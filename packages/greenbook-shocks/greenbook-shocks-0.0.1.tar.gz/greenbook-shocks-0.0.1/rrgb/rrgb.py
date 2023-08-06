import calendar
import os
import importlib.resources
import re
import tempfile
import urllib
from datetime import date, datetime
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

import datapungi_fed as dpf
import numpy as np
import pandas as pd
import urllib3
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression


class RRGB:
    """
    RRGB Class
    Romer and Romer GreenBook class containing Romer and Romer 2004 data and updated Greenbook Data from the Philly Fed.
    """
    def __init__(self, rrfname='RomerandRomerDataAppendix.xls', rr_override=True) -> None:
        """
        RRGB Class
        Romer and Romer GreenBook class containing Romer and Romer 2004 data and updated Greenbook Data from the Philly Fed.
        Parameters
        ----------
        rr_override: Bool, default=True
            If True, replace greenbook data from Philly Fed with overlapping data from the original Romer and Romer dataset, including NA's,
            otherwise only fill in missing greenbook data with nonmissing Romer and Romer data.

        """
        self.get_fomc_dates()
        self.read_romer_romer(fname=rrfname)
        self.read_all_gbs()
        self.gb_data()
        self.merge_gb_target()
        self.fill_gb_na_rr()
        if rr_override:
            self._rr_gb_replace()
        return None

    def _read_header(self, h):
        """
        Helper function to process table headers from FOMC website to return meeting information
        """
        # Header examples
        # 1) h = 'January 27-28 Meeting - 2015'
        # 2) h = 'January 31-February 1 Meeting - 1995'
        # 3) h = 'February 7 Conference Call - 2009'
        # 4) h = 'October 16 (unscheduled) - 2013'
        # 5) h = 'April/May 30-1 Meeting - 2013'
        # 6) h = 'October 21, 22, 23, 26, 27, 28, 29, and 30 Conference Calls - 1987'

        # Year
        year = re.findall('[0-9]{4}', h)[0]
        h = re.sub(r'\s{,}-\s{,}[0-9]{4}', '', h)
        # Meeting type
        mtgtype = [h.find(mtype) > 0 for mtype in ['(unscheduled)', 'Conference Call']]
        h = re.sub(r'\s{,}(Meeting|\(unscheduled\)|Conference Call(s){,})', '', h)

        # Date range. Check for unique cases
        # First check for April/May 30-1 date and manualy return correct value
        if h.strip() == 'April/May 30-1':
            return date(2013, 4, 30), date(2013, 5, 1), False, False
        # Check for black monday conference calls. Manually split the header
        # and call the outer function on each indivdually
        if h.strip() == 'October 21, 22, 23, 26, 27, 28, 29, and 30':
            for hi in [21, 22, 23, 26, 27, 28, 29, 30]:
                self._read_header(f'October {hi} Conference Call - 1987')
            return

        # Now format based on 3 standard cases (cases 1-3)
        daterange = h.split('-')
        if len(daterange) == 1:
            daterange.append('')
        startmonth = daterange[0].split()[0]
        startday = daterange[0].split()[1]
        enddate = daterange[1].split()
        if len(enddate) == 2:
            endmonth = enddate[0]
            endday = enddate[1]
        elif len(enddate) == 1:
            endmonth = startmonth
            endday = enddate[0]
        elif len(enddate) == 0:
            endmonth = startmonth
            endday = startday
        startdate = date(int(year), datetime.strptime(startmonth, "%B").month, int(startday))
        enddate = date(int(year), datetime.strptime(endmonth, "%B").month, int(endday))
        # print(f'{startdate} - {enddate}')
        return startdate, enddate, mtgtype[0], mtgtype[1]

    def get_fomc_dates(self):
        """
        Creates the _fomc_dates dataframe.
        Fields:
        mtg_start and mtg_end are the start and end dates for each FOMC meeting, scrapped from the FOMC website.
        unscheduled, cancelled, notation_vote, conference_call are booleans for the type of meeting
        has_gb signifies if the meeting has an associated greenbook
        mtg_year and mtg_number create unique identifiers for meetings with greenbooks
        gb_pub_date is the publishing date of the greenbook, taken from Philly Fed.
        """
        # Greenbook Dates
        gb_dates = pd.read_excel(
            'https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/greenbook-data/greenbook_publication_dates_web.xlsx?la=en&hash=02104A132EEFCE6C867E4CA3AB023333',
            index_col='ORDER', usecols=['ORDER', 'FOMC Meeting', 'Greenbook Publication Date'])
        gb_dates.index.rename('order', inplace=True)
        gb_dates[['mtg_year', 'mtg_number']] = gb_dates.loc[:, 'FOMC Meeting'].str.split('mtg', expand=True)
        gb_dates.drop('FOMC Meeting', axis=1, inplace=True)
        gb_dates.rename(columns={'Greenbook Publication Date': 'gb_pub_date'}, inplace=True)
        for v in ['mtg_number', 'mtg_year']:
            gb_dates[v] = pd.to_numeric(gb_dates[v])

        # Get the FOMC dates
        # Read in the dates that are not historical
        print('Reading FOMC meeting dates')
        http = urllib3.PoolManager()
        url = 'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'
        r = http.request('GET', url)
        raw = r.data
        soup = BeautifulSoup(raw, 'html.parser')
        panels = soup.find_all('div', {'class': 'panel panel-default'})
        years = []
        months = []
        dates = []
        for p in panels:
            yearstr = p.find_all('div', {'class': 'panel-heading'})[0].text
            innermonth = [x.text for x in p.find_all('div', {'class': 'fomc-meeting__month'})]
            years.extend(np.repeat(re.findall('[0-9]+', yearstr)[0],  len(innermonth)))
            months.extend(innermonth)
            dates.extend([x.text for x in p.find_all('div', {'class': 'fomc-meeting__date'})])

        # Parse the dates and calculate meeting type
        # SEP is processed, but not saved in the final data
        df = pd.DataFrame({'year': years, 'month': months, 'dates': dates})
        df['sep'] = df['dates'].str.find('*') > 0
        df['dates'] = df['dates'].str.replace('*', '', regex=False)
        df['unscheduled'] = df['dates'].str.find('(unscheduled)') > 0
        df['dates'] = df['dates'].str.replace('(unscheduled)', '', regex=False)
        df['cancelled'] = df['dates'].str.find('(cancelled)') > 0
        df['dates'] = df['dates'].str.replace('(cancelled)', '', regex=False)
        df['notation_vote'] = df['dates'].str.find('(notation vote)') > 0
        df['dates'] = df['dates'].str.replace('(notation vote)', '', regex=False)
        df[['startday', 'endday']] = df['dates'].str.split('-', expand=True)
        df.loc[df['endday'].isna(), 'endday'] = df.loc[df['endday'].isna(), 'startday']
        df[['startmonth', 'endmonth']] = df['month'].str.split('/', expand=True)
        df.loc[df['endmonth'].isna(), 'endmonth'] = df.loc[df['endmonth'].isna(), 'startmonth']

        # Create start and end meeting dates
        # Replace abbreviated months with full month names first
        df.replace({m: calendar.month_name[list(calendar.month_abbr).index(m)] for m in calendar.month_abbr}, inplace=True)
        df['mtg_start'] = df.apply(lambda row: date(int(row['year']), datetime.strptime(
            row['startmonth'], "%B").month, int(row['startday'])), axis=1)
        df['mtg_end'] = df.apply(lambda row: date(int(row['year']), datetime.strptime(
            row['endmonth'], "%B").month, int(row['endday'])), axis=1)
        df = df.loc[:, ['mtg_start', 'mtg_end', 'unscheduled', 'cancelled', 'notation_vote']]

        # Move to historical dates
        # First find all the years
        url = 'https://www.federalreserve.gov/monetarypolicy/fomc_historical_year.htm'
        raw = urllib.request.urlopen(url).read()
        urls = re.findall('href="/monetarypolicy/fomchistorical[0-9]{4}.htm"', str(raw))
        urlyears = (re.findall(r'[0-9]{4}', url)[0] for url in urls)

        # For each year, scrape the associated page
        headers = []
        for year in urlyears:
            url = f'https://www.federalreserve.gov/monetarypolicy/fomchistorical{year}.htm'
            print(url)
            soup = BeautifulSoup(http.request('GET', url).data, 'html.parser')
            if int(year) <= 2010:
                panels = soup.find_all('div', {'class': 'panel panel-default'})
                headers.extend([p.find('div', {'class': 'panel-heading'}).text for p in panels])
            else:
                panels = soup.find_all('div', {'class': 'panel panel-default panel-padded'})
                headers.extend([p.find('h5', {'class': 'panel-heading panel-heading--shaded'}).text for p in panels])

        # Process each page and then concocatnate them
        # Drop NA because the black monday meetings have an extra empty row
        historical_data = pd.DataFrame([self._read_header(h) for h in headers], columns=['mtg_start',
                                       'mtg_end', 'unscheduled', 'conference_call']).dropna()
        for v in ['mtg_start', 'mtg_end']:
            historical_data[v] = pd.to_datetime(historical_data[v])
        # Redefine Sept 15 as a notation vote to better align with 2020 data
        historical_data['notation_vote'] = False
        historical_data.loc[historical_data['mtg_start'] == datetime(2003, 9, 15), 'notation_vote'] = True
        # Combine datasets and format dates
        full_data = pd.concat([df, historical_data], ignore_index=True).fillna(False)
        for v in ['mtg_start', 'mtg_end']:
            full_data.loc[:, v] = pd.to_datetime(full_data.loc[:, v])
        full_data.loc[:, 'mtg_year'] = full_data.loc[:, 'mtg_start'].dt.year
        tmp = full_data.query('~unscheduled & ~notation_vote & ~conference_call').copy()
        tmp.loc[:, 'mtg_number'] = tmp.groupby('mtg_year').cumcount() + 1
        full_data = full_data.join(tmp.loc[:, ['mtg_number']], how='left')
        full_data = pd.merge(full_data, gb_dates, on=['mtg_year', 'mtg_number'], how='outer')
        full_data.loc[:, 'has_gb'] = ~full_data.loc[:, 'gb_pub_date'].isna()
        full_data.sort_values(['mtg_start'], inplace=True)
        full_data.reset_index()
        self._fomc_dates = full_data
        return full_data

    def read_romer_romer(self, fname=None):
        if fname is None:
            ref = importlib.resources.files('rrgb').joinpath('data/rr.pkl.gz')
            rr = pd.read_pickle(ref, 'gzip')
        else:
            rr = pd.read_excel(fname, sheet_name='DATA BY MEETING')
            rr['MTGDATE'] = rr['MTGDATE'].astype('str').str.zfill(6)
            rr['year'] = rr['MTGDATE'].apply(lambda x: '19' + x[-2:]).astype('int')
            rr['month'] = rr['MTGDATE'].apply(lambda x: x[0:2]).astype('int')
            rr['day'] = rr['MTGDATE'].apply(lambda x: x[2:-2]).astype('int')
            rr['mtgdate'] = pd.to_datetime(rr[['year', 'month', 'day']])
            rr.drop(['MTGDATE', 'year', 'month', 'day'], axis=1, inplace=True)
            rr_rename = {'GRADM': 'gPGDPM', 'GRAD0': 'gPGDP0', 'GRAD1': 'gPGDP1', 'GRAD2': 'gPGDP2',
                         'IGRDM': 'IgPGDPM', 'IGRD0': 'IgPGDP0', 'IGRD1': 'IgPGDP1', 'IGRD2': 'IgPGDP2',
                         'GRAYM': 'gRGDPM', 'GRAY0': 'gRGDP0', 'GRAY1': 'gRGDP1', 'GRAY2': 'gRGDP2',
                         'IGRYM': 'IgRGDPM', 'IGRY0': 'IgRGDP0', 'IGRY1': 'IgRGDP1', 'IGRY2': 'IgRGDP2',
                         'GRAU0': 'UNEMP0'}
            rr.rename(columns=rr_rename, inplace=True)
            rr.set_index('mtgdate', inplace=True)
        self._rr = rr
        return rr

    @staticmethod
    def _read_gb(fname):
        """
        Reads in the greenbook forecast data and reshapes to long format
        Returns the forecast of a single variable at multiple horizons for multiple dates in long format
        Day is calculated weird to avoid setting column to scallar when there is no data in the excel file
        """
        df = pd.DataFrame(pd.read_excel(fname, index_col='Date').stack()).reset_index()
        df.columns = ['valuedate', 'var_fdate', 'value']
        df.loc[:, 'variable'] = df.loc[:, 'var_fdate'].apply(lambda x: x[0:-9])
        df.loc[:, 'forecastdate'] = pd.to_datetime(df.loc[:, 'var_fdate'].apply(lambda x: x[-8:]), format='%Y%m%d')
        df.loc[:, 'year'] = np.floor(df.loc[:, 'valuedate'])
        df.loc[:, 'month'] = 3 * np.round(10*(df.loc[:, 'valuedate'] - np.floor(df.loc[:, 'valuedate'])))
        df.loc[:, 'day'] = np.divide(np.floor(df.loc[:, 'valuedate']), np.floor(df.loc[:, 'valuedate']))
        df.loc[:, 'valuedate'] = pd.to_datetime(df.loc[:, ['year', 'month', 'day']]) + pd.tseries.offsets.QuarterEnd()
        return df.loc[:, ['variable', 'forecastdate', 'valuedate', 'value']]

    def read_all_gbs(self, gb_all_url='https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/greenbook-data/gbweb/gbweb_all_column_format.zip?la=en&hash=22851EFA1EF12BDB30474720752BB409'):
        """
        Create the _gb_forecasts dataframe containing the greenbook forecasts for all variables in long format.
        Parameters
        ---
        gb_all_url : str, default='https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/greenbook-data/gbweb/gbweb_all_column_format.zip?la=en&hash=22851EFA1EF12BDB30474720752BB409'
            url pointing the the zip file containing the greenbook forecasts from philadelphia fed. The default is the current url
            Runs _read_gb for each database and manually adjusts the forecast date for several observatios where there is a discrepancy between the
            meeting dates from the Philly Fed and the FOMC. Also calculates the forecast horizon in quarters for each observation
        """
        tmpdir = tempfile.mkdtemp()
        with urlopen(gb_all_url) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall(tmpdir)
        gbdf = pd.concat([self._read_gb(fname) for fname in os.scandir(tmpdir)], ignore_index=True)
        gb_fdate_adjs = {np.datetime64('1991-06-28'): np.datetime64('1991-06-26'),
                         np.datetime64('1992-06-26'): np.datetime64('1992-06-24'),
                         np.datetime64('1993-01-29'): np.datetime64('1993-01-27'),
                         np.datetime64('1994-06-30'): np.datetime64('1994-06-29')}
        gbdf['forecastdate'].replace(gb_fdate_adjs, inplace=True)
        # Add in two forecasts from Romer and Romer that are not in the Philly Fed data
        # 2/4/1969 Meeting
        RR_additons = [
            {
                'variable': ['gPGDP', 'gRGDP'],
                'forecastdate': datetime(1969, 1, 29),
                'valuedate': datetime(1969, 9, 30),
                'value': [4.2, 1.4]
            }
        ]
        gbdf = gbdf.append([pd.DataFrame(x) for x in RR_additons], ignore_index=True)
        gbdf['horizon'] = np.round(
            (gbdf['valuedate'] - (gbdf['forecastdate'] + pd.tseries.offsets.QuarterEnd(0))) / np.timedelta64(3, 'M')).astype(int)
        self._gb_forecasts = gbdf
        return gbdf

    def gb_data(self):
        """
        Create the _gb data frame containing the gb data in wide format.
        Indexed by forecastdata/mtg_end and valuedata/horizon.
        Fields are the gb forecasts and the innovations to the gb forecasts
        """
        gb = pd.merge(
            self._gb_forecasts[['variable', 'forecastdate', 'valuedate', 'horizon', 'value']],
            self._fomc_dates[['mtg_end', 'gb_pub_date']],
            left_on='forecastdate', right_on='gb_pub_date', how='left').drop(
            columns='gb_pub_date')
        gb = gb.set_index(['forecastdate', 'mtg_end', 'valuedate', 'horizon',
                          'variable']).squeeze().unstack(level='variable')
        # gb.sort_index(level=['valuedate', 'forecastdate', 'mtg_end'], inplace=True)
        # Make the greenbook innovations
        gbdates = gb.reset_index().loc[:, 'forecastdate'].sort_values().drop_duplicates().reset_index(drop=True)
        mtg_maps = pd.concat([gbdates, gbdates.shift(-1).rename('next_forecastdate')], axis=1).dropna().set_index('forecastdate')
        gb_old = gb.join(mtg_maps, how='inner').set_index('next_forecastdate', append=True)
        gb_old.index.rename(['prev_forecastdate', 'mtg_end', 'valuedate', 'horizon', 'forecastdate'], inplace=True)
        gb_old = gb_old.droplevel(['prev_forecastdate', 'horizon', 'mtg_end'])
        gb_old = gb.filter(items=[]).join(gb_old)
        gbI = gb - gb_old
        gbI.rename(columns=lambda x: "I" + x, inplace=True)
        gb = gb.join(gbI)
        gb.sort_index(level=['forecastdate', 'horizon'])
        self._gb = gb
        return gb

    def merge_gb_target(self):
        """
        Add the change in the target rate and the old level of the target rate to the _gb dataframe.
        For the period overlapping with the Romer and Romer dataset use the target rate variables from there.
        For the period after the Romer and Romer dataset use data from FRED. The target rate is well defined post 1995.
        Also realign some meeting dates during the Romer and Romer period with the R&R dataset being definitive.
        """
        # First calculate changes in the target rate for all dates
        freddata = dpf.data("5240bbe3851ef2d1aaffd0877d6048dd")
        fftarget = pd.concat([freddata.series(s).rename(columns={s: 'fftarget'}) for s in ['DFEDTAR', 'DFEDTARL']])
        fftarget['DTARG'] = fftarget['fftarget'].shift(-1).diff(3)
        fftarget['OLDTARG'] = fftarget['fftarget'].shift(2)

        # Split data into pre-Romer and Romer, Romer and Romer, and Post Romer and Romer samples
        self._gb.sort_index(level='forecastdate', inplace=True)
        rr = self._rr.sort_index().reset_index()[['mtgdate', 'DTARG', 'OLDTARG']]

        gb_pre_rr = self._gb.query('forecastdate.dt.year < @rr["mtgdate"].min().year')
        gb_rr = self._gb.query('@rr["mtgdate"].min().year <= forecastdate.dt.year <= @rr["mtgdate"].max().year')
        gb_post_rr = self._gb.query('forecastdate.dt.year > @rr["mtgdate"].max().year')

        # Merge the Romer and Romer Target rate change data onto our data and fix meeting dates
        gb_rr = pd.merge_asof(gb_rr, rr, left_on='forecastdate', right_on='mtgdate',
                              direction='nearest').set_index(gb_rr.index)
        gb_rr.index.set_levels(levels=gb_rr.loc[:, 'mtgdate'].values, level=1, verify_integrity=False)
        gb_rr.reset_index(inplace=True)
        gb_rr.loc[gb_rr['mtg_end'].isna(), 'mtg_end'] = gb_rr.loc[gb_rr['mtg_end'].isna(), 'mtgdate']
        gb_rr.drop(columns='mtgdate', inplace=True)
        gb_rr.set_index(['forecastdate', 'mtg_end', 'valuedate', 'horizon'], inplace=True)

        # Merge the change in target rate onto the post romer and romer data
        gb_post_rr = pd.merge(
            gb_post_rr, fftarget[['DTARG', 'OLDTARG']],
            left_on=gb_post_rr.index.get_level_values('mtg_end'),
            right_on='date').set_index(
            gb_post_rr.index).drop(
            ['date'],
            axis=1)

        # Concatenate the early and late data together
        gb = pd.concat([gb_pre_rr, gb_rr, gb_post_rr]).sort_index(level=['forecastdate', 'horizon'])
        self._gb = pd.concat([gb_rr, gb_post_rr]).sort_index(level=['forecastdate', 'horizon'])
        return gb

    def fill_gb_na_rr(self):
        """
        Replace NA values in _gb with corresponding values from _rr dataframe.
        """
        rr_gb_mapper = {
            'gPGDPM': 'gPGDP_-1',
            'gPGDP0': 'gPGDP_0',
            'gPGDP1': 'gPGDP_1',
            'gPGDP2': 'gPGDP_2',
            'gRGDPM': 'gRGDP_-1',
            'gRGDP0': 'gRGDP_0',
            'gRGDP1': 'gRGDP_1',
            'gRGDP2': 'gRGDP_2',
            'UNEMP0': 'UNEMP_0',
            'IgPGDPM': 'IgPGDP_-1',
            'IgPGDP0': 'IgPGDP_0',
            'IgPGDP1': 'IgPGDP_1',
            'IgPGDP2': 'IgPGDP_2',
            'IgRGDPM': 'IgRGDP_-1',
            'IgRGDP0': 'IgRGDP_0',
            'IgRGDP1': 'IgRGDP_1',
            'IgRGDP2': 'IgRGDP_2',
            'IUNEMP0': 'IUNEMP_0',
        }
        # Convert _rr to long format with same variable names as _gb
        rr_cover = self._rr.filter(list(rr_gb_mapper.keys()), axis=1).rename(columns=rr_gb_mapper)
        colnames = [x.split("_") for x in rr_cover.columns]
        colnames = [(var, int(h)) for var, h in colnames]
        rr_cover.columns = pd.MultiIndex.from_tuples(colnames, names=['variable', 'horizon'])
        rr_cover.index.rename('mtg_end', inplace=True)
        rr_cover = rr_cover.stack(dropna=False)
        pd.DataFrame(index=self._gb.index).join(rr_cover, on=['mtg_end', 'horizon'])
        self._rr_cover = rr_cover.join(pd.DataFrame(index=self._gb.index))
        self._rr_cover = self._rr_cover.reorder_levels(self._gb.index.names)
        # Do the filling
        self._gb.fillna(self._rr_cover, inplace=True)

    def _rr_gb_replace(self):
        """
        Replace all values in _gb with corresponding values in _rr including NA's.
        Use this function to make _gb data match exactly to Romer and Romer 2004 data for regressions.
        This Mostly affects 1972 data where Romer and Romer are missing 2 qtr ahead forecasts for 1972-07-12 and 1972-09-13 meetings.
        """
        self._gb.loc[self._rr_cover.index.intersection(self._gb.index), self._rr_cover.columns] = self._rr_cover.loc[self._rr_cover.index.intersection(self._gb.index), self._rr_cover.columns]

    def print_vars(self):
        print(list(self._gb.columns))
        return list(self._gb.columns)

    def estimate_shocks(
            self, start=datetime(1969, 3, 1),
            end=datetime(1996, 12, 31),
            drop_zlb=None,
            control_vars={'OLDTARG': [0],
                          'gRGDP': list(range(-1, 3)),
                          'IgRGDP': list(range(-1, 3)),
                          'gPGDP': list(range(-1, 3)),
                          'IgPGDP': list(range(-1, 3)),
                          'UNEMP': [0]},
            model=LinearRegression()
            ):
        """
        Estimate the Romer and Romer Greenbook Narative Shocks
        Parameters
        ----------
        start : datetime, default=datetime(1969, 3, 1)
            Start date for the regression sample. Defaults to R&R 2004 sample.
        end : datetime, default=datetime(1996, 12, 31)
            End date for the regression sample. Defaults to R&R 2004 sample.
        drop_zlb : None or ['estimation', 'prediction', 'both'], default=None
            When to drop observations at the ZLB:
                - if None, keep all observations at the ZLB.
                - if 'estimation', drop observations at the ZLB only when estimating linear regression model.
                - if 'prediction', drop observations at the ZLB only when estimating the residuals from the linear regression model.
                - if 'both', drop observations at the ZLB at both steps
            The ZLB is defined as any meeting where the old target rate was below 25 basis points.
        control_vars : Dict(str: list[int]), default={'OLDTARG': [0],
                          'gRGDP': list(range(-1, 3)),
                          'IgRGDP': list(range(-1, 3)),
                          'gPGDP': list(range(-1, 3)),
                          'IgPGDP': list(range(-1, 3)),
                          'UNEMP': [0]}
            Dictionary specifying the linear model. The keys are the forecast variables to include and the
            values are lists containing the forecasts horizons to include for that variable. Defaults to R&R 2004 variables.
        mode : Sklearn Regression Model, default=LinearRegression()
            SKlearn regression model for estimating prediction model.
        Returns
        -------
        rrshocks: DataFrame
            Dataframe containing the narrative shocks, indexed by the FOMC meeting date.
        Details
        -------
        Uses the data in the _gb dataframe as the input into the estimation and prediction of the model. Additional variables can be added to this dataframe
        before calling this method if needed. The model can be any sklearn regression model that impliments the fit and predict methods including pipelines.
        """
        if (drop_zlb is not None) and (drop_zlb not in ['estimation', 'prediction', 'both']):
            raise ValueError(
                f'drop_zlb = {drop_zlb}.\ndrop_zlb must be None or one of ["estimation", "prediction", "both"].')
        query_elements = [f'(variable == "{key}" & horizon == {value})' for key, value in control_vars.items()]
        query_elements.append('(variable == "DTARG" & horizon == 0)')
        df_long = self._gb.reset_index().drop(
            columns=['forecastdate', 'valuedate']).melt(
            id_vars=['mtg_end', 'horizon']).set_index(
            ['mtg_end', 'horizon', 'variable']).query(' | '.join(query_elements))
        df_wide = df_long.reset_index().pivot(index='mtg_end', columns=['variable', 'horizon'], values='value')
        df_wide.query('@start <= mtg_end <= @end', inplace=True)
        zlb_mtgs = list(df_long.query('horizon == 0 & variable == "OLDTARG" & value < 0.25').index.get_level_values('mtg_end'))
        df_wide.dropna(inplace=True)
        if drop_zlb in ['both', 'estimation']:
            self._reg_df = df_wide.query('mtg_end != @zlb_mtgs')
        else:
            self._reg_df = df_wide.copy()
        y = self._reg_df.loc[:, 'DTARG']
        X = self._reg_df.drop(level=0, columns='DTARG')
        model.fit(X, y)
        if drop_zlb in ['both', 'prediction']:
            self._pred_df = df_wide.query('mtg_end != @zlb_mtgs')
        else:
            self._pred_df = df_wide.copy()
        ytilde = self._pred_df.loc[:, 'DTARG']
        Xtilde = self._pred_df.drop(level=0, columns='DTARG')
        resid = ytilde - model.predict(Xtilde)
        resid.columns = ['rrshock']
        self.rrshocks = resid
        self._rr_reg_model = model
        return resid

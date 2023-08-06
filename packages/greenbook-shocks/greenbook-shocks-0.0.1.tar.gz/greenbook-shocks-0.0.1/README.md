# GreenbookNarrativeShocks

This package estimates up to date Romer and Romer Greenbook Narrative shocks, originally from
[A New Measure of Monetary Shocks: Derivation and Implications](https://www.aeaweb.org/articles?id=10.1257/0002828042002651), 2004.

# Installation
`pip install greenbookshocks`

# Usage
The core class is the `RRGB` (Romer and Romer GreenBook) class. When this class is instantiated it
downloads the data necessary to create the Romer and Romer Greenbook narrative shock series.
The user needs to supply the original data appendix file from
[Romer and Romer](https://www.aeaweb.org/articles?id=10.1257/0002828042002651), (2004)
with the path specified by the `rrfname` argument in the class call, which defaults
to `rrfname='RomerandRomerDataAppendix.xls'`. The user then needs to call the `estimate_shocks()` method.
The following code exactly replicates the original shock series.

```python
from rrgb import RRGB
from datetime import datetime
# Assemble Data
rrgb = RRGB(rrfname='RomerandRomerDataAppendix.xls', rr_override=True)
# Estimate shocks
shocks = rrgb.estimate_shocks()
```

The final shock series will be indexed by the meeting date. The user may then aggregate the
series up with her preferred aggregation method.

# Advanced Usage
The original dataset used in [Romer and Romer](https://www.aeaweb.org/articles?id=10.1257/0002828042002651), (2004)
was drawn from the text of the Greenbook itself. This package supplements this data with the Greenbook datasets
provided by the Federal Reserve Bank of Philadelphia which is drawn from internal forecast materials prepared by
the Federal Reserve Board of Governors staff. This dataset varies slightly from the Romer and Romer dataset. For
earlier periods, the Romer and Romer dataset contains a few additional forecast observations which this package
always uses. In 1972, the Philadelphia Fed dataset has additional observations. By default this package does not
use these observations, allowing it to exactly match the original Romer and Romer dataset. If the user would like
to use the full dataset then she may specify the `rr_override` argument as `False`, e.g. `RRGB(rr_override=False)`,
the default behavior is True.

# Custom models
The `estimate_shocks()` method allows the user to specify the date range of the shocks, the control variables
used in the regression, wether or not to drop ZLB periods in estimation and the model to use to form the predicted
shocks. See the docstring for additional information.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="greenbook-shocks",  # Replace with your own username
    version="0.0.1",
    author="Joe Saia",
    author_email="joe5saia@gmail.com",
    description="Estimates the Greenbook narrative shocks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joe5saia/GreenbookNarrativeShocks",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'sklearn',
        'datapungi_fed',
        'urllib3',
        'bs4',
        'sklearn',
        'openpyxl'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={'': ['data/rr.pkl.gz']},
)

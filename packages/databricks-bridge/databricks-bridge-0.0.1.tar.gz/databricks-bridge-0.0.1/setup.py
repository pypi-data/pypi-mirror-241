from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Databricks read and write with sql connection'
LONG_DESCRIPTION = 'Databricks read and write data from and to databricks tables via insert statement direct write, pandas or spark dataframes to insert statement conversion write'

# Setting up
setup(
    name="databricks-bridge",
    version=VERSION,
    author="Y-Tree (Saeed Falowo)",
    author_email="saeed@y-tree.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'databricks-sql-connector', 'pyspark'],
    keywords=['python', 'databricks', 'pyspark', 'sql', 'dataframe'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

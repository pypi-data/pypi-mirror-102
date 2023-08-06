# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['edfi_lms_ds_loader', 'edfi_lms_ds_loader.helpers']

package_data = \
{'': ['*'], 'edfi_lms_ds_loader': ['scripts/mssql/*', 'scripts/postgresql/*']}

install_requires = \
['configargparse>=1.2.3,<2.0.0',
 'edfi-lms-extractor-lib==1.0.0a4',
 'edfi-lms-file-utils==1.0.0b16',
 'errorhandler>=2.0.1,<3.0.0',
 'pandas>=1.1.2,<2.0.0',
 'psycopg2>=2.8.6,<3.0.0',
 'pyodbc>=4.0.30,<5.0.0',
 'python-dotenv>=0.15.0,<0.16.0',
 'sqlalchemy==1.3.23',
 'sqlparse>=0.4.1,<0.5.0']

setup_kwargs = {
    'name': 'edfi-lms-ds-loader',
    'version': '1.0.0a0',
    'description': 'Ed-Fi LMS Toolkit Data Store Loader',
    'long_description': '# lms-ds-loader\n\nThe Ed-Fi LMS Data Store Loader is a utility for loading CSV files in the\nLearning Management System Unified Data Model (LMS-UDM) into a Learning\nManagement System Data Store (LMS-DS) database.\n\nThe application processes each file in the input file system by date order, as\nindicated in the file name. If a record is in a file one day, and missing on the\nnext day, then the system "soft deletes" that record by setting the current\ntimestamp into the `deletedat` column. This functionality requires that a root\nlevel directory only contains files for one LMS provider. Thus if an education\norganization uses multiple LMS providers, then each LMS Extractor needs to write\nfiles to a separate, dedicated directory, and the LMS DS Loader must be run once\nfor each extractor\'s output directory.\n\nLimitations as of March 2021:\n\n* Data loads only supports SQL Server (tested on MSSQL 2019).\n* Only supports loading User files.\n* Does not perform updates or deletes, and will throw an error if trying to\n  reload an existing record.\n\n## Getting Started\n\n1. SQL Server support requires the Microsoft ODBC 17 driver, which is newer than\n   the ones that come with most operating systems.\n   * Windows: `choco install sqlserver-odbcdriver`\n   * [Linux\n     instructions](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)\n     (has not been tested yet)\n1. Requires Python 3.9+ and Poetry.\n1. Install required Python packages:\n\n   ```bash\n   poetry install\n   ```\n\n1. The database account used when running the tool needs to be a member of the\n   following roles in the destination database:\n\n   * db_datareader\n   * db_datawriter\n   * db_ddladmin\n\nNote that the tool automatically manages deployment of the LMS-DS tables into\nthe destination database, under the `lms` schema.\n\n## Running the Tool\n\nFor detailed help, execute `poetry run python edfi_lms_ds_loader -h`.\n\nSample call using full integrated security, loading from the sample files\ndirectory:\n\n```bash\npoetry run python edfi_lms_ds_loader --server localhost --dbname lms_toolkit --useintegratedsecurity --csvpath ../../docs/sample-out\n```\n\n## Developer Notes\n\n### Dev Operations\n\n1. Style check: `poetry run flake8`\n1. Static typing check: `poetry run mypy .`\n1. Run unit tests: `poetry run pytest`\n1. Run unit tests with code coverage: `poetry run coverage run -m pytest`\n1. View code coverage: `poetry run coverage report`\n\n_Also see\n[build.py](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit/blob/main/docs/build.md)_ for\nuse of the build script.\n\n### Adding New Migrations\n\n1. Create SQL Server and PostgreSQL SQL scripts under\n   `edfi_lms_ds_loader/scripts/<engine name>`, using the same file name for\n   both. Start from the artifact created by MetaEd, and then update the script\n   with these modifications:\n   * Remove the `Id` column and the default constraint for that column.\n   * Add a `DeletedAt` column as a nullable `Datetime2`.\n   * Duplicate the table definition and prefix the duplicate with "stg_".\n   * In the staging table, change the `xyzIdentifier` primary key column name to\n     `StagingId`, and leave out the `DeletedAt` column.\n1. Use `;` (semi-colon) terminators at the end of each SQL statement for both\n   languages. Do not use `GO` in the SQL Server files, as the application is not\n   coded to parse it.\n1. Add the new script name to the `MIGRATION_SCRIPTS` constant at the top of\n   `edfi_lms_ds_loader/migrator.py`.\n\n### Adding New Files Uploads\n\n1. Create the required table and staging table in a new migration.\n1. Ensure that the `file-utils` shared library correctly maps the data types for\n   the new file.\n1. Update the `edfi_lms_ds_loader/loader_facade.py` to pull in the additional\n   file type and upload it.\n\n## Legal Information\n\nCopyright (c) 2021 Ed-Fi Alliance, LLC and contributors.\n\nLicensed under the [Apache License, Version 2.0](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit/blob/main/LICENSE) (the "License").\n\nUnless required by applicable law or agreed to in writing, software distributed\nunder the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR\nCONDITIONS OF ANY KIND, either express or implied. See the License for the\nspecific language governing permissions and limitations under the License.\n\nSee [NOTICES](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit/blob/main/NOTICES.md) for\nadditional copyright and license notifications.\n',
    'author': 'Ed-Fi Alliance, LLC and contributors',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://techdocs.ed-fi.org/display/EDFITOOLS/LMS+Toolkit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

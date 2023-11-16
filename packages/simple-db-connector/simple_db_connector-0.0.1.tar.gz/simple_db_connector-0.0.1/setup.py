from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Simple database connector for python'
LONG_DESCRIPTION = 'Python module for simple connection and editing of databases.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="simple_db_connector", 
        version=VERSION,
        author="Rene Schwertfeger",
        author_email="<mail@reneschwertfeger.de>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["mysql_connector_repackaged"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'database', 'connector', 'simple', 'mysql', 'mariadb', 'sqlite', 'sql', 'connector', 'db', 'database-connector', 'database-connection', 'database-connection-python', 'database-connector-python', 'database-connection-mysql', 'database-connector-mysql', 'database-connection-sqlite', 'database-connector-sqlite', 'database-connection-mariadb', 'database-connector-mariadb', 'database-connection-sql', 'database-connector-sql'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
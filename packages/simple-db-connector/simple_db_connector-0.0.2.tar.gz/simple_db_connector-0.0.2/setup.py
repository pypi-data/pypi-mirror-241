from setuptools import setup, find_packages

VERSION = '0.0.2' 
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
        install_requires=["mysql-connector"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'database', 'connector', 'simple', 'mysql', 'mariadb', 'sqlite', 'sql', 'connector', 'db', 'database-connector'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
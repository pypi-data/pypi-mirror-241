import os
# run test script in file directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from simple_db_connector import database


# Call the database class
db = database.database(
    os.environ["db_url"],
    os.environ["db_user"],
    os.environ["db_password"],
    os.environ["db_port"],
    os.environ["db_name"],
)

# Connect python string to the database type
string_type = type("string").__name__
print(db.data_typ_converter(string_type))

# Connect python int to the database type
int_type = type(1).__name__
print(db.data_typ_converter(int_type))

# Connect python float to the database type
float_type = type(1.1).__name__
print(db.data_typ_converter(float_type))

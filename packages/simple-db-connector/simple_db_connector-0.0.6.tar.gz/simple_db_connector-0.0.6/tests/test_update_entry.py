import os
from simple_db_connector import database
import decimal
import datetime


# Call the database class
db = database(
    os.environ["db_url"],
    os.environ["db_user"],
    os.environ["db_password"],
    os.environ["db_port"],
    os.environ["db_name"],
)

# Example Table Name 
table_name =  "cars_table"  

# Example Search Parameter
search_parameter =  {
	"manufacture"  :  "toyoat"
}  
# Example Update Parameter
search_parameter =  {
	"manufacture"  :  "toyota"
} 

# Example Table creation 
db.update_entry(table_name, search_parameter)

# Example Table Name 
table_name =  "cars_table"  

# Example Search Parameter
search_parameter =  {
	"manufacture"  :  "toyoat",
	"model" : "Aygo X yalp",
}  
# Example Update Parameter
search_parameter =  {
	"manufacture"  :  "toyota",
	"model" : "Aygo X play",
} 

# Example Table creation 
db.update_entry(table_name, search_parameter)
import mysql.connector
from flaskext.mysql import MySQL
from Config import dbConfig

mysql = MySQL()

def init_app(app):
    mysql.init_app(app)





def check_database_connection():
    try:
        # Get a cursor for the database connection
        cursor = mysql.get_db().cursor()
        cursor.close()  # Close the cursor
        return True
    except Exception as e:
        # Handle the exception if the database connection fails
        return str(e)




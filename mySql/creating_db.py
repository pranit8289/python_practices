import mysql.connector

import mysql_connection as mycon
import settings as config


dataBase = mysql.connector.connect(
    host=config.MySQLClass.host,
    user=config.MySQLClass.user,
    passwd=config.MySQLClass.passwd)

# # This area where we are writing the SQL logic
# Creating Data base names practice_db
cursor_obj = dataBase.cursor()
print(f"[INFO] obj - {cursor_obj}")
cursor_obj.execute("CREATE DATABASE practice_db")

# # Disconnecting from the server
cursor_obj.close()
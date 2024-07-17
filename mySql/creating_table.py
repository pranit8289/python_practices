import mysql.connector
import settings as config


dataBase = mysql.connector.connect(
    host=config.MySQLClass.host,
    user=config.MySQLClass.user,
    passwd=config.MySQLClass.passwd)

# # This area where we are writing the SQL logic

# Creating cursor object
cursor_obj = dataBase.cursor()

# Selecting database before creating table otherwise we might get folloeing error
# mysql.connector.errors.ProgrammingError: 1046 (3D000): No database selected

select_db = """USE practice_db;"""
cursor_obj.execute(select_db) 

# Writing the query for creating table
studentTable = """CREATE TABLE STUDENT(
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   );"""
  
# Executing table creation query
cursor_obj.execute(studentTable) 

# # Disconnecting from the server
cursor_obj.close()
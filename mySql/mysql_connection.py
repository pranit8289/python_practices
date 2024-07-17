# importing required libraries
import mysql.connector
import settings as config

class MakeSQLConnection():
    def __init__(self, host=config.MySQLClass.host, user=config.MySQLClass.user, passwd=config.MySQLClass.passwd):
        self.host=host
        self.user=user
        self.passwd=passwd

    def check_conenction_to_db(self,):
        dataBase = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd)
        return dataBase
    
if __name__ == "__main__":

    mSqlObj = MakeSQLConnection(host="localhost", user="root", passwd="ind@mh12")
    # print(dir(mSqlObj)) # testing out the connection 
    # # This area where we are writing the SQL logic
    cursor_obj = mSqlObj.check_conenction_to_db()
    print(cursor_obj)


    # # Disconnecting from the server
    cursor_obj.close()

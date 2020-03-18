import datetime as dt
import random as rnd
import pyodbc as pyodbc

# variables

try:
    userid = str(input("Please enter userid: "))
    login_name = str(input("Please enter login name: "))
    pwd = str(input("Please enter your password: "))
except:
    raise ValueError("You have entered incorrect login details, please check and retry!")

server = 'tcp:bistudiosqlserver.database.windows.net'
database = 'Securesdb'
username = 'username'
password = 'pwd'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+
                      ';PWD='+password)
cursor = cnxn.cursor()


# Sample select query
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

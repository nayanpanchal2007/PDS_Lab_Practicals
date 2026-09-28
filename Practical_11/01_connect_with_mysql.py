import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nayan2007@"
)
if connection.is_connected():
    print("Connection Successful")

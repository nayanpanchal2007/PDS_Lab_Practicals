import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nayan2007@"
)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS college")
print("Database Created")
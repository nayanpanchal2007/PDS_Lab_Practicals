import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nayan2007@",
    database="college"
)
print("Connected Successfully")
cursor = connection.cursor()
query = """
CREATE TABLE IF NOT EXISTS student(
roll INT PRIMARY KEY,
name VARCHAR(50),
department VARCHAR(30),
marks FLOAT
)
"""
cursor.execute(query)
print("Table Created")

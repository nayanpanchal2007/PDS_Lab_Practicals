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
INSERT INTO student
VALUES(101,'Amit','CSE',85)
"""
cursor.execute(query)
connection.commit()
print("Record Inserted")

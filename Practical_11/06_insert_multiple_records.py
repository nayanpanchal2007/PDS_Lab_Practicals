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
VALUES(%s,%s,%s,%s)
"""
records = [
(102,"Neha","IT",92),
(103,"Rahul","ECE",78),
(104,"Priya","CSE",95)
]
cursor.executemany(query, records)
connection.commit()
print("Multiple Records Inserted")

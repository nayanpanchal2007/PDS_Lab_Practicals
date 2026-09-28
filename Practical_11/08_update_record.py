import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nayan2007@",
    database="college"
)
cursor = connection.cursor()
query = """
UPDATE student
SET marks=90
WHERE roll=101
"""
cursor.execute(query)
connection.commit()
print("Record Updated")

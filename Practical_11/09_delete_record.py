import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nayan2007@",
    database="college"
)
cursor = connection.cursor()
query = """
DELETE FROM student
WHERE roll=103
"""
cursor.execute(query)
connection.commit()
print("Record Deleted")

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nayan2007@",
    database="college"
)
cursor = connection.cursor()
roll = int(input("Enter Roll Number: "))
query = "SELECT * FROM student WHERE roll=%s"
cursor.execute(query, (roll,))
record = cursor.fetchone()
print(record)

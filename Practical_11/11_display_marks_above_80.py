import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nayan2007@",
    database="college"
)
cursor = connection.cursor()
cursor.execute(
"SELECT * FROM student WHERE marks > 80"
)
records = cursor.fetchall()
for student in records:
    print(student)

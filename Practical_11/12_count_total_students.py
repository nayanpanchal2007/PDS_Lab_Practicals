import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nayan2007@",
    database="college"
)
cursor = connection.cursor()
cursor.execute(
"SELECT COUNT(*) FROM student"
)
count = cursor.fetchone()
print("Total Students =", count[0])

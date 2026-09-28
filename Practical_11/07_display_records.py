import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nayan2007@",
    database="college"
)
print("Connected Successfully")
cursor = connection.cursor()
cursor.execute("SELECT * FROM student")
result = cursor.fetchall()
for row in result:
    print(row)

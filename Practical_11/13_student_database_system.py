import mysql.connector
connection = mysql.connector.connect(
host="localhost",
user="root",
password="Nayan2007@",
database="college"
)
cursor = connection.cursor()
while True:
    print("\n------ Student Database System ------")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        roll = int(input("Roll: "))
        name = input("Name: ")
        dept = input("Department: ")
        marks = float(input("Marks: "))
        query = """
        INSERT INTO student
        VALUES(%s,%s,%s,%s)
        """
        cursor.execute(query, (roll, name, dept, marks))
        connection.commit()
        print("Student Added Successfully")
    elif choice == 2:
        cursor.execute("SELECT * FROM student")
        records = cursor.fetchall()
        for row in records:
            print(row)
    elif choice == 3:
        roll = int(input("Roll Number: "))
        marks = float(input("New Marks: "))
        query = """
        UPDATE student
        SET marks=%s
        WHERE roll=%s
        """
        cursor.execute(query, (marks, roll))
        connection.commit()
        print("Record Updated Successfully")
    elif choice == 4:
        roll = int(input("Roll Number: "))
        query = """
        DELETE FROM student
        WHERE roll=%s
        """
        cursor.execute(query, (roll,))
        connection.commit()
        print("Record Deleted Successfully")
    elif choice == 5:
        connection.close()
        print("Thank You")
        break
    else:
        print("Invalid Choice")

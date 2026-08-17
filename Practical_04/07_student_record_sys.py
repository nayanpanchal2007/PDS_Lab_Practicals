students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students[roll] = {
        "Name": name,
        "Marks": marks
    }
print("\nStudent Records")
for roll in students:
    print(roll, students[roll])

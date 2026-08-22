with open("students.txt", "a") as file:
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        file.write(f"{name},{marks}\n")
print("Student Records Saved Successfully")

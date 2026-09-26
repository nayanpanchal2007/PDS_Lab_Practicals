marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
    raise ValueError("Marks should be between 0 and 100.")
print("Marks =", marks)

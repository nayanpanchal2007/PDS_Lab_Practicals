n = int(input("Enter number of students: "))
total = 0
for i in range(n):
    marks = float(input(f"Enter marks of Student {i+1}: "))
    total += marks
average = total / n
print("Average Marks =", round(average, 2))

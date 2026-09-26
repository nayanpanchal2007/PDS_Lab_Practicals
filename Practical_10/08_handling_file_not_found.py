try:
    file = open("student.txt")
    print(file.read())
except FileNotFoundError:
    print("Requested file not found.")

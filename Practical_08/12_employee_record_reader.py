try:
    with open("employees.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Employee file does not exist.")

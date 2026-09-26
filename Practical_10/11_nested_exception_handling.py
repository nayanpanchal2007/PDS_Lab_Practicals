try:
    try:
        number = int(input("Enter number: "))
        print(100 / number)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")

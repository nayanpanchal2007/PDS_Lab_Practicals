try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ZeroDivisionError:
    print("Division by zero.")
except ValueError:
    print("Invalid input.")

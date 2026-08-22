try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Result =", result)
finally:
    print("Program Executed Successfully")

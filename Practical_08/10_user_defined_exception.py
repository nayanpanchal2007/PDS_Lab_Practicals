class InvalidAgeError(Exception):
    pass
age = int(input("Enter age: "))
try:
    if age < 18:
        raise InvalidAgeError
    print("Eligible")
except InvalidAgeError:
    print("Age must be at least 18 years.")

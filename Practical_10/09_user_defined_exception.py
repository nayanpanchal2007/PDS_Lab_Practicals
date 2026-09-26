class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError
    print("Eligible for voting.")
except InvalidAgeError:
    print("Age must be at least 18 years.")

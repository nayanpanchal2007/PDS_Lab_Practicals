password = input("Enter password: ")
if len(password) >= 8:
    if any(ch.isdigit() for ch in password):
        if any(ch.isupper() for ch in password):
            print("Strong Password")
        else:
            print("Add at least one uppercase letter")
    else:
        print("Add at least one digit")
else:
    print("Password should contain at least 8 characters")

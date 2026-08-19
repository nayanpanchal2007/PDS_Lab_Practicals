correct_pin = "1234"
attempt = 0
while attempt < 3:
    pin = input("Enter ATM PIN: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
        attempt += 1
if attempt == 3:
    print("Card Blocked")

balance = 5000
amount = float(input("Enter withdrawal amount: "))
if amount <= balance:
    balance -= amount
    print("Transaction Successful")
    print("Remaining Balance = ₹", balance)
else:
    print("Insufficient Balance")

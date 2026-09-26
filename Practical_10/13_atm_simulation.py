balance = 10000
try:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if amount > balance:
        raise Exception("Insufficient balance.")
    balance -= amount
    print("Transaction Successful")
    print("Remaining Balance =", balance)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Transaction Failed:", e)
finally:
    print("Thank you for using our ATM.")

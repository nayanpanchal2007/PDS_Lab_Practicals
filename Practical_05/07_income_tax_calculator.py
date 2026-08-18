income = float(input("Enter annual income: "))
if income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 0.05
elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10
else:
    tax = 45000 + (income - 900000) * 0.15
print("Estimated Tax = ₹", tax)

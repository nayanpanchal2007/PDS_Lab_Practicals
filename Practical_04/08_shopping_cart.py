cart = []
while True:
    item = input("Enter Item (type 'exit' to finish): ")
    if item.lower() == "exit":
        break
    cart.append(item)
print("\nShopping Cart")
for item in cart:
    print(item)

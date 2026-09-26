try:
    numbers = [5, 10, 15, 20]
    index = int(input("Enter index: "))
    print(numbers[index])
except IndexError:
    print("Invalid index.")
except ValueError:
    print("Please enter an integer.")

age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
experience = int(input("Enter years of experience: "))
if age >= 21:
    if salary >= 30000:
        if experience >= 2:
            print("Loan Approved")
        else:
            print("Insufficient Experience")
    else:
        print("Salary Requirement Not Met")
else:
    print("Age Requirement Not Met")

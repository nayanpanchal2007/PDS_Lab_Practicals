import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll", "Name", "Marks"])
    writer.writerow([101, "Amit", 85])
    writer.writerow([102, "Priya", 91])
print("CSV File Created")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

import pickle
student = {
    "Name": "Hardi",
    "Age": 20,
    "Branch": "Computer"
}
with open("student.dat", "wb") as file:
    pickle.dump(student, file)
with open("student.dat", "rb") as file:
    data = pickle.load(file)
print(data)

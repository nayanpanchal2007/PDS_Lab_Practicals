import numpy as np
marks = np.array([85,78,92,67,88,95,73])
print("Marks :", marks)
print("Average :", np.mean(marks))
print("Highest :", np.max(marks))
print("Lowest :", np.min(marks))
print("Students Scoring Above Average")
for mark in marks:
    if mark > np.mean(marks):
        print(mark)

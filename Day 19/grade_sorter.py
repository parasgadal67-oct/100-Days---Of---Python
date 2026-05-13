# This program sorts student on basis of grades
students = [
    ("Paras", 98),
    ("Ravi", 86),
    ("Simran",75),
    ("Joshep",88),
    ("Allan", 96)
]
students.sort(key = lambda x : x[1], reverse= True)
print(students)
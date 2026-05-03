# a dictionary of students
students = {"Sandeep" : 13,
            "Rihsab" : 15,
            "Arav" : 14,
            "Pawan" : 12}

#getting the age or particular student
print(students.get("Arav"))

# adding new value to existing dictionary
students.update({"Arya" : 16})

# changing the age of particular student
students.update({"Arav" : 16})

# seperating key and values of dictionary
print(students.keys())
print(students.values())
print(students)
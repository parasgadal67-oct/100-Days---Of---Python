students = ["Aman","Sara","Ravi"]
classes = ["English","Mathematics","Science"]
for i in range(len(students)):
    print(students[i])
    for subject in classes:
        print(students[i], "is in",subject)

#using sort() in the list to sort students according to their marks.
name_1 = input("Enter the student name: ")
marks_1 = int(input("Enter the marks: ")) 

name_2 = input("Enter the student name: ")
marks_2 = int(input("Enter the marks: ")) 

name_3 = input("Enter the student name: ")
marks_3 = int(input("Enter the marks: ")) 

name_4 = input("Enter the student name: ")
marks_4 = int(input("Enter the marks: ")) 

name_5 = input("Enter the student name: ")
marks_5 = int(input("Enter the marks: "))

names = []
names.append(name_1)
names.append(name_2)
names.append(name_3)
names.append(name_4)
names.append(name_5)

marks = []
marks.append(marks_1)
marks.append(marks_2)
marks.append(marks_3)
marks.append(marks_4)
marks.append(marks_5)
print(names)
marks.sort(reverse=True)
print(marks)
print("Top 3 Scorers:")
print("1st:",marks[0])
print("2nd:",marks[1])
print("3rd:",marks[2])
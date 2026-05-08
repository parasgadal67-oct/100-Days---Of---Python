# creating student attendance tracker
students = ["Rahul" , "Sneha" , "Pankaj"]
attendance = [
    ["P","A","P"],
    ["A","P","P"],
    ["P","P","A"]
]
for i in range(len(students)):
    print(students[i])
    for day in attendance[i]:
        print(" ",day)
    
    
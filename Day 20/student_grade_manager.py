# creating student grade manager
students = {"Arnav": 95,
            "Parveen": 87,
            "Sonika": 97,
            "Rahul": 96,
            "Tanya": 98,
            "Arjun": 89,
            "Ayush": 99}
def student_grade_manager():
    for student in students:
        grade = students[student]
        print(f"{student}: {grade}")
        
    student = list(students.values())
    def average():
        return sum(student) / len(student)
    print(round(average(), 2))
    student_sort = sorted(students.items(), key= lambda x: x[1], reverse=True)
    print(student_sort)
    highest_grade = max(students, key= lambda x: x[1])
    print(f"Highest: {highest_grade}-{students[highest_grade]}")
    lowest_grade = min(students, key= lambda x: x[1])
    print(f"Lowest: {lowest_grade}-{students[lowest_grade]}")

student_grade_manager()

   
  

   
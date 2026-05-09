# sorting  grade with function
name = input("Enter the student name: ")
marks_obtained = float(input("Enter the marks obtained: "))
percentage = marks_obtained/500 * 100
def student_grade(percentage):

    if percentage >= 90:
        print(f" {name}, Your percentage is {percentage}%,")
        print("You have obtained A Grade")
    elif percentage >= 80:
        print(f" {name},Your percentage is {percentage}%,")
        print("You have obtained B Grade")
    elif percentage >= 70:
        print(f" {name},Your percentage is {percentage}%,")
        print("You have obtained C Grade")
    elif percentage >= 60:
        print(f" {name},Your percentage is {percentage}%,")
        print("You have obtained D Grade")
    elif percentage >= 33:
        print(f" {name},Your percentage is {percentage}%,")
        print("Passed with E Grade")
    else :
        print(f" {name}, Your percentage is {percentage}")
        print("FAIL")
        
        
student_grade(percentage) 
    
    
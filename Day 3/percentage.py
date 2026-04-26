#calculating the percentage of given subjects 
english = int(float(input("Enter the marks obtained in English: ")))
maths = int(float(input("Enter the marks obtained in Maths: ")))
science = int(float(input("Enter the marks obtained in Science: ")))
hindi = int(float(input("Enter the marks obtained in Hindi: ")))
social_studies = int(float(input("Enter the marks obtained in Social Studies: ")))

total_marks = english + maths + science + hindi + social_studies
percentage = round((total_marks / 500) * 100, 2)

if percentage >= 90:
    print(f"Congratulations ! you have scored {percentage}% and have A grade")
    
elif percentage >= 80:
    print(f"Congratulations ! you have scored {percentage}% and have B grade")
    
elif percentage >= 70:
    print(f"Congratulations ! you have scored {percentage}% and have C grade")
    
elif percentage >= 60:
    print(f"Congratulation ! you have scored {percentage}% and have Dgrade")
    
else:
    print(f"Sorry ! you have scored {percentage}% and have F grade :()")

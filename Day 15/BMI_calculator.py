# creating BMI calculator 
def convert_height():
    choice = input("Isyour height is in feet or in meters?(f / m): ")
    if choice == "f":
        feet = float(input("Enter height in feet: "))
        meters = feet * 0.3048
        return meters
    else:
        meters = float(input("Enter height in meter: "))
        return meters
    
def BMI_calculator():
    age = int(input("Enter your age: "))
    if age < 18:
        print("Currently unable to calculate.(MINOR)")
        return 
    height = convert_height()
    weight = float(input("Enter your weight: "))
    
    BMI = weight / (height**2)
    BMI = round(BMI, 2) 
    print(f"Your BMI is : {BMI}")   
    
    if age >= 18 and age <= 60:
        if BMI < 18:
            print("Category: Underweight.")
        elif BMI < 25:
            print("Category: Normal/Healthy.")
        elif BMI < 30:
            print("Category: Overweight.")
        else:
            print("Category: Obese.") 
    else:
        if BMI < 23:
            print("Underweight according to your age.")
        elif BMI < 30:
            print("Normal/Healthy according to your age.")
        else:
            print("You are in range of obese.")
            
            
BMI_calculator()                   
            
         
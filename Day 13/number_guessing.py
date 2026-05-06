# creating number guessing game
correct_number = 97
number = int(input("Enter the the number: "))
while not number == correct_number:
    print("It is not a correct number.")
    if number > correct_number:
        print ("The number is bigger.Think of some smaller no.")
    elif number < correct_number:
        print("The number is smaller.Think of  little bigger no.") 
    number = int(input("Enter the the number: "))
print(f"Excellent, here is your correct no. {correct_number}")
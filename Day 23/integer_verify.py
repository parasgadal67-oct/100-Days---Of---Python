#creating a vefification fumction to verify if the given input is is integer or not.
def get_number():
    while True:
        user_input = input("Enter the number:  ")
        try:
            number = int(user_input)
            print(f" your given number is {number} is an integer.")
            again = input("Do you want to continue?(yes/no):  ")
            if again.lower() != "yes":
               break
        except ValueError:
            print("Please enter the digits only! Try again .")
        
get_number()
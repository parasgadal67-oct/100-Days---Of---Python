# creating safe calculator using exception handling
def safe_calculator():
    while True:
        try:
            num_1 = int(input("Enter the first number: "))
            num_2 = int(input("Enter the second number: "))
            operator = input("Enter the operator(+,-,*,/): ")
            if operator == "+":
                result = num_1 + num_2
                print(f'The result of {num_1} + {num_2} is {result}')
            elif operator == "-":
                result = num_1 - num_2
                print(f'The result of {num_1} - {num_2} is {result}')
            elif operator == "*":
                result = num_1 * num_2
                print(f'The result of {num_1} * {num_2} is {result}')
            elif operator == "/":
                result = num_1 / num_2
                print(f'The result of {num_1} / {num_2} is {result}')
            else:
                print("Invalid operator! Enter a valid operator(+ , - , * , /).")
                
                repeat = input("Do you want to calculate again?(yes/no): ")
                if repeat.lower() != "yes":
                    print("Thankyou for using calculator! See you again.")
                    break        
        except ValueError:
              print("Invalid input! please enter a valid number.")
        except ZeroDivisionError:
              print("Error! Division by zero isn't allowed.")
        except Exception as e:
              print(f"Something went wrong!try again. Error: {e}")        
safe_calculator()
             
             
            
        
        

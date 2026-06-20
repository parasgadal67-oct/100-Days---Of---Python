# organising the previous project calculator with modules
import calculator_operations
from calculator_operations import add, subtract, multiply, divide
while True:
        
        try:
            num_1 = int(input("Enter the first number: "))
            num_2 = int(input("Enter the second number: "))
            operator = input("Enter the operator for calculation(+,-,*,/): ")   
            if operator == "+":
                result = add(num_1, num_2)
            elif operator == "-":
                result = subtract(num_1, num_2)
            elif operator == "*":
                result = multiply(num_1, num_2)
            elif operator == "/":
                result = divide(num_1, num_2)
            else:
                print("Invlid Operator!")
                continue
            
            print(f"Result: {result}")
            
        except ValueError:
            print("Invalid input. Numbers only")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            
        again = input("Want to calculate again(yes/no):  ")
        if again.lower()!= "yes":
            print("THANKYOU FOR USING CALCULATOR.")
            break 
            
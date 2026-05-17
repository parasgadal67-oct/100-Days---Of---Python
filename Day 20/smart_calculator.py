# Day 20 creating smart calculator
def calculator():
    while True:
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        operator = input("Enter the operator(+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator. Please enter a valid operator.")
        if operator == '+':
          sum = num_1 + num_2
          print(f"The sum of {num_1} and {num_2} is = {sum}")
        elif operator == '-':
          difference = num_1 - num_2
          print(f"The difference of {num_1} and {num_2} is = {difference}")
        elif operator == '*':
          product = num_1 * num_2
          print(f"The product of the {num_1} and {num_2} is = {product:.2f}")
        elif operator == '/':
          if num_2 == 0:
            print("Numbercan't be divided by zero.")
          else:
            quotient = num_1 / num_2
            print(f"The quotient of {num_1} and {num_2} is = {quotient:.2f}")
        decision = input("Do you want to continue ? (yes / no): ")
        if decision == "no":
            print("Thankyou for using calculator.")
            break
        else:
            continue
            
            
calculator()            
        
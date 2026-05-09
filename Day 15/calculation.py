# calculating numbers using function
def calculator():
    x = float(input("Enter the number: "))
    y = float(input("Enter the number: "))
    z = input("Enter the operator: ")
    
    if z == "+":
     return x + y
    elif z == "-":
     return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        if y == 0:
            print("Can't be divided by zero.")
        return x / y
    else:
        print("Invalid")


result = calculator()
print(f"Your answer is: {result}")
# calculating number with operators
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
operator = input("Which operator are you using ?: ")

if operator == "+":
    print(round(number_1 + number_2 , 2))
elif operator == "-":
    print(round(number_1 - number_2 , 2))
elif operator == "*":
    print(round(number_1 * number_2 , 2))
elif operator == "/":
    if number_2 == 0:
        print("Can't be divided by zero.")
    else:
        print(round(number_1 / number_2 , 2))

else:
    print("Invalid operator.")
    
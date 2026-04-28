# checking the number is gerater then zero or not
# if number is greater than 0 output positive 

number = float(input("Enter the number: "))

if  number > 0:
    print(f"The {number} is Positive.")
elif number < 0:
    print(f"The {number} is Negative.")
elif number == 0:
    print("Zero")

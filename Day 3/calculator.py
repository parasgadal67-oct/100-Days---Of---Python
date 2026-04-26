#building an interest calculator
principal = int(float(input("Enter the principal amount: ")))
rate = int(float(input("Enter the rate of interest: ")))
time = int(float(input("Enter the time in years: ")))
simple_interest = (principal * rate * time) / 100

total_amount = principal + simple_interest

print(f"The simple interest is : {simple_interest}")
print(f"The total amount after {time} years is: {total_amount}")

if total_amount > 100000:
    print("Large Amount")
    
elif total_amount > 50000:
    print("medium amount")
    
else:
    print("Small amount")
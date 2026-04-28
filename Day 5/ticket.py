#creating ticket calculator
passenger_name = input("Enter the passenger's name: ")
age = int(input("Enter passenger's age: "))
weekend = input("Is it weekend ?(yes.no): ").lower()
price = 0
if age <= 0:
    price = 0
elif age <= 12:
    price = 50
elif age <= 17:
    price = 100
elif age <= 59:
    price = 200
else: 
    price = 80
    
if weekend == "yes":
    surge = price * 20 /100
    price = price + surge
    print(f" {passenger_name}, your ticket price is Rs {price}")
else:
    print(f" {passenger_name}, your ticket price is Rs {price}")
        
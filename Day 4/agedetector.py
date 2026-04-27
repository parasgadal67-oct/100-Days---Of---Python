# building an age detector using input function.

name = input("Enter the name of the person: ")
age = int(input("Enter the age: "))

if age >= 18:
    print(f" {name}, you are an adult.")
    
else:
    print(f" {name}, you are minor.")
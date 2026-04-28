#  creating an age checker 
username = input("Enter your name: ")
user_age = int(input("Enter your age: "))

if user_age >= 60:
 print(f" {username}, You are a Senior Citizen")
elif user_age >= 18:
    print(f"{username}, You are an Adult")
elif user_age >= 13:
    print(f"{username}, You are Teenager")
elif user_age >= 0:
    print(f"{username}, You are Child")
else:
    print(f"Invalid")

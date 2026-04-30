#creating a system for login using coditionals
user_name1 = "Parasgadal67-oct"
username = input("Username: ")
password_1 = "1234567890"
password = input("Password: ")

if username == user_name1:
    if password == password_1:
        print("ACCESS-GRANTED")
        print(f"WELCOME {user_name1}")
    else:
        print("ACCESS-DENIED")
        print("CHECK USERNAME / PASSWORD")
else:
    print("ACCESS-DENIED")
    print("CHECK USERNAME / PASSWORD")
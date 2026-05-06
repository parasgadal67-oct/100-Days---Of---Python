# password checker
user_password = "python123"
password = int(input("Enter the password: "))
while not password == user_password:
    print("ACCESS-DENIED!")
    password = int(input("Enter the password: "))
    
print("ACCESS-GRANTED!")
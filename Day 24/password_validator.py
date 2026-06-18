# creating password  vallidator through  exception.
class CustomException(Exception):
    pass
def password_checker():
        user_name = input("Enter your username: ")
        password = input("Enter your pasword: ")
        if len(password) < 8:
            raise CustomException("Password must be at least 8 characters.")
        elif not any(char.isdigit() for char in password):
            raise CustomException("Password must contain at least a digit.")
        elif not any(char.isupper() for char in password):
            raise CustomException("Password must contain at least an uppercase letter.")
        elif not any(char.islower() for char in password):
            raise CustomException("Password must contain at least a lowercase letter.")
        elif not any(char in "!@#$%^&*()-_=+[]{}/;:,.<>?}" for char in password):
            raise CustomException("Password must contain at least a special character.")
        else:
            return f"Access Granted {user_name}!"
while True:
 try:  
    result = password_checker()
    print(result)
    break
 except CustomException as e:
     print(f"Error: {e}")
    
def check_password(password):
    
    def check_uppercase():
        return any(c.isupper() for c in password)
    def check_digit():
        return any(c.isdigit() for c in password)
    def check_length():
        return len(password)>=8
    if check_uppercase() and check_digit() and check_length():
        return " Strong Password"
    else:
        if not check_uppercase():
            print(" Password must contain at least one uppercase letter.")
        if not check_digit():
            print("Password must contain at least one digit.")
        if not check_length():
            print("Passsword must contain at least 8 characters.")
            
        
print(check_password("Paras123"))         
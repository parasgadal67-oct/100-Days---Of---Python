# creating temprature converter
def conversion():
    choice = input("Which conversion you want?(C to F, F to C, C to K): ")
    if choice == "C to F":
        C = float(input("Enter temperature in celsius: "))
        C_F = (C * 9/5) + 32
        return f"{C_F} degree F"
    elif choice == "F to C":
        F = float(input("Enter temperature in fahrenheit: "))
        F_C = (F - 32) * 5/9
        return f"{F_C} degree C"
    elif choice == "C to K":
        C = float(input("Enter temperature celsius: "))
        C_K = C + 273.15
        return f"{C_K} Kelvin"
    
print(conversion())
        
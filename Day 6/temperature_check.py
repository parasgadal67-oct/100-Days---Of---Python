# checking person having fever or not or low body temperature.
temperature = float(input("Whats the temperature ?: "))
fever = 37.5 
low = 36 

if temperature >= 37.2:
    print(f"Your body temperature is {temperature}, Fever")
elif temperature <= 36:
    print(f"Your body temperature is {temperature}, Low")
else:
    print("Normal.")
     


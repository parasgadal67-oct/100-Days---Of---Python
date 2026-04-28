# creating money tracker for savings
salary = int(input("What is your salary ?: "))
expenses = int(input("How much do you spent?: "))

if expenses > salary:
    print("You are in debt.")
elif expenses >= salary * 90/100:
    print("Warning ! Very low savings.")
elif expenses >= salary * 70/100:
    print("Moderate savings.")
else:
    print("Good savings 😊. ")
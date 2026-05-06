#creating functional atm using while loop
balance = 1000
while True:
    user = input("How can i help you ?: ")
    if user == "check-balance":
        print(f"Your account balance is {balance}.")
    elif user == "withdraw":
        amount = int(input("Enter your amount: "))
        if amount > balance:
            print("Insufficient-balance.")
        else:
            balance = balance - amount
            print("Withdrawal-successful.")
            print(balance)
    elif user == "exit":
        break
print("Thankyou for banking with us.")
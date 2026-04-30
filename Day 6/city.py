# checking the user's city is valid or not
user_country = "India"
user_state = "Uttarakhand".title()
user_city = "Dehradun".title()
city = input("Enter the city: ").title()
if city == user_city:
    state = input("Enter the state: ").title()
    if state == user_state:
        print("LOCATION VERIFIED.")
        print(f"User is from {user_city},{user_state}.")
    else:
        print("State mismatched.")
else:
    print("City is not in our database.")
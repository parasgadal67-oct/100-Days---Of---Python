#creating voterid checker.
voter_name = input("Enter voter name: ")
voter_age = int(input("Enter voter age: "))

if voter_age >= 18:
    voter_id = input("Do you have voter id ?:(Yes / No):")
    if voter_id == "Yes" or "yes" or "YES":
        print("You are eligible to Vote.")
    else:
        print("Get voter id first.")
else:
    print("You are MINOR can't Vote")
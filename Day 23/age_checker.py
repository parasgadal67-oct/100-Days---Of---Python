# creating age checking function using exception handling
def age_checker():
    while True:
        try:
            age = int(input("Enter the age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
        except ValueError as e:
            print(f"Invalid input! {e}")
        else:
            print(f"Your age is {age}.")
            break
age_checker()
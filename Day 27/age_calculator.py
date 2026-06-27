#Age_Calculator
#Using concepts : datetime module, while loop, try/except, and conditionals.
from datetime import date, datetime
while True:
    try:
        birth_date = input("Enter your Date Of Birth(DD-MM-YYYY): ")
        date_of_birth = datetime.strptime(birth_date, "%d-%m-%Y")
        date_of_birth = date_of_birth.date()
        today = date.today()
        difference = today - date_of_birth

        # for years months and  days we will add;
        years = difference.days // 365
        remaining_days = difference.days % 365
        months = remaining_days // 30

        if date_of_birth > today:
            print("We can't predict future! enter the valid date.")
        elif date_of_birth < date(1950, 1, 1):
            print("Seems too old / ancient ! enter after the 1950 year.")
        elif years == 0 and months == 0:
            print("Months and years cannot be zero! Enter again")
        else:
            print(f"You lived {difference.days} till now date {date.today()}.")
            print(f"You are {years} years, {months} months old. ")
            break
            
    except ValueError:
        print("Enter the Valid Value!") 
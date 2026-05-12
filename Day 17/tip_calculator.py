# using nested function to calculate tip and total bill amount
def tip_calculator():
    bill_amount = float(input("Enter the bill amount: "))
    tip = float(input("What is the tip percentage?: "))
    def calculate_tip():
           return bill_amount * (tip / 100)
         
    def calculate_total(tip):
         return bill_amount + tip
    tip_amount = calculate_tip()
    total_amount = calculate_total(tip_amount)
    return tip_amount, total_amount

tip_amount, total_amount = tip_calculator()
print(f"Tip_amount: {tip_amount:.2f}")
print(f"Total amount: {total_amount:.2f}")

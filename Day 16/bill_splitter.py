# demostrating bill splitting through funtion parameter.
def bill_splitter(total, tip_percent= 10, people= 2):
     tip = total * tip_percent/100
     total_with_tip = total + tip
     per_person = total_with_tip / people
     return per_person
print(bill_splitter(3000,))
    
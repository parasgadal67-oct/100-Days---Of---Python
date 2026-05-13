#This program sorts  a list of numbers
num = input("Enter the list of numbers: ").split(",")
number = []
for x in num:
    number.append(int(x))
    
number.sort(key = lambda x : x)
print(number)

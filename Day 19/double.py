# This program doubles each number in a list
num = input("enter the list of numbers:")
num = num.split(",")
map(int, num)
number = [int(x) for x in num]
numbers = list(map(lambda x: x * 2, number))
print(numbers)
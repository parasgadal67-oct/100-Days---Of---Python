# Filtering the even  and odd numbers with help of dictionary comprehension
numbers = [1, 2, 34, 75, 48, 96, 99, 17, 78, 10, 15]
num_check = {num :("Even" if num % 2 == 0 else "odd") for num in numbers}
print(num_check)
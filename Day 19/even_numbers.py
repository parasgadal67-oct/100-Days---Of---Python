# finding even numbers using lambda functon  and filter 
number = input("Enter the list of numbers: ")
number = number.split(",")
number = [int(x) for x in number]
even_numbers = list(filter(lambda x: x % 2 == 0, number))
print(even_numbers)
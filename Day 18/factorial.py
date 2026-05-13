def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter the number: "))

print(factorial(number))
print(f"The factorial of {number} is {factorial(number)}")
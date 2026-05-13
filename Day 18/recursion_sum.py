def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)
number = int(input("Enter the number: "))

print(sum(number))
print(f"The sum of {number} is {sum(number)}")
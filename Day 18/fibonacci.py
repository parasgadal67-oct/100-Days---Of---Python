def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter Fibonacci term: "))
print(f" The fibonacci term of {n} is {fibonacci(n)}")  
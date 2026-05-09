# with the help of function  findong number info (even / odd)
def number_info(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

number_info(-18)
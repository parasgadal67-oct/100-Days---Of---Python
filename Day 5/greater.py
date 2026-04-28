# finding which one is greater
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
num_3 = float(input("Enter the third number: "))
if num_1 > num_2 and num_1 > num_3 :
    print(f" {num_1} is greater.")
elif num_2 > num_1 and num_2 > num_3 :
    print(f" {num_2} is greater.")
elif num_3 > num_1 and num_3 > num_2 :
    print(f" {num_3} is greater.")
else:
    print("All numbers are equal.")
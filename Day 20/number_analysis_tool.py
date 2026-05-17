# creating number analysis tool
def number_analysis_tool():
     num = int(input("Enter the number: "))
     def even_numbers():
         if num % 2 == 0:
             print(f"{num} is an even number.")
         else:
             print(f"{num} is an odd number.")
             
     def factorial(num):
        if num < 0:
            print("factorial not defined for negative numbers")
        else:
            if num == 0 or num == 1:
                return 1
            else:
                return num * factorial(num-1)
     def doubling(num):
          return (lambda x: x * 2)(num)
     even_numbers()
     print(f"Factorial of {num} is {factorial(num):.2f}")
     print(f"Doubling of {num} is {doubling(num)}")
     
number_analysis_tool()
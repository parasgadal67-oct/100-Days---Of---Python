# print the multiplication table using function
def times_table(n):
    for i in range(1,11):
         result = n * i
         print(f" {n} * {i} = {result}")
         
times_table(5)

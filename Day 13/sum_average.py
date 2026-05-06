# calculating sum and avage of given numbers
sum = 0
count = 0 
while True :
  number = input("Enter the number: ")
  if number == "done":
    break
  sum = sum + int(number)
  count = count + 1
print(sum)
print(sum/count)
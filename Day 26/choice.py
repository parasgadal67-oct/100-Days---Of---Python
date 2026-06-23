# picking choice of fruit through random.choice
import random
def fruit_choice(items):
    return random.choice(items)
fruits = ["gooseberry","plum","apple","orange","pineaple","banana"]
print(fruit_choice(fruits))

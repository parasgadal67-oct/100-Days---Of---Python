# creating a dice roller through random module.
import random
while True:
        def roll_dice(sides=6):
            return random.randint(1, sides)

        print(f"You rolled: {roll_dice()}")
        print(f"D20 roll:{roll_dice(20)}")
        again = input("Wanna roll again?(yes/no): ")
        if again.lower()!= "yes":
            break
        else:
            continue
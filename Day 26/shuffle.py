# shuffling the fruits using random.shuffle
import random
while True:
        def shuffle_list(cards):
            random.shuffle(cards)
            return cards
        deck = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
        print(shuffle_list(deck)) 
        again = input("Wanna shuffle again?(yes/no): ")
        if again.lower()!= "yes":
            break
        else:
            continue
# coin flipper  with random module
import random
while True:
        def coin_flip(coin):
            return random.choice(coin)
        result = ["Heads", "Tails"]
        print(f"You got {coin_flip(result)}")
        again = input("Do you want another flip?(yes/no): ")
        if again.lower()!= "yes":
            break  
        else:
            continue
    
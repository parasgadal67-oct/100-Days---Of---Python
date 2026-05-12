def number_doubler(n):
    def validate():
        return n>0
    if validate():
        print(f"Result: {n * 2}")
    else:
        print("Invalid number.")
        
number_doubler(48)        
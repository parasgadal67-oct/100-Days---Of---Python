def apply_discount(price, discount_percent):
    def calculate_discount():
        return price * (discount_percent / 100)
    def validate():
        return price > 0
    
    if validate():
        discount_price = price - calculate_discount()
        print(f"Discounted Price: {discount_price:.2f}")
    else:
        print("Invalid price.")
        
apply_discount(1000, 15)        
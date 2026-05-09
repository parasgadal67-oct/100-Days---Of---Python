def shopping_cart(item, price, quantity=1, discount=0):
    item_name = item
    orignal_price = price
    net_quantity = quantity
    total_price = orignal_price * net_quantity
    discount_amount = total_price * discount/100
    final_price = total_price - discount_amount
    return f"{item_name}:{net_quantity}*{orignal_price}={final_price}({discount}%off)"
print(shopping_cart("Milk",35,2)) 
     
     
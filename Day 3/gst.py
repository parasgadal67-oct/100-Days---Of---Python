#calculating gst 
item = input("what is this item ?: ")
item_price = int(float(input("Enter the price of an item: ")))
gst_rate = int(float(input("Enter the GST rate: ")))
gst_amount = (item_price * gst_rate) / 100
total_price = item_price + gst_amount


print(f"The GST amount is: {gst_amount}")
print(f"The total price including GST is: {total_price}")
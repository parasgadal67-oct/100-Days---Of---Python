#creating atm mini system
correct_card = 123456789012
correct_pin = 2567
card = int(input("Enter the card name: "))
pin = int(input("Enter the pin: "))

 
if card == correct_card:
      if pin == correct_pin:
          amount = int(input("Enter the amount: "))
          if amount >= 500:
              print("TRANSACTION SUCCESSFUL.")
          else:
              print("ISUFFICIENT BALANCE.")
      else:
          print("INVALID PIN.")
else:
    print("INCORRECT CARD.")
              
              
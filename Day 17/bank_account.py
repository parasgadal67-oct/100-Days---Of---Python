def bank_account(name, balance):
     def deposit(amount):
         nonlocal balance
         balance += amount
     def withdraw(amount):
         nonlocal balance
         if balance >=amount: 
             balance -= amount
             print(f"withdrawn: {amount}")
         else:
             print("Insufficient funds.")
             
     def get_balance():   
         return balance
     print(f"Account: {name}")
     deposit(5000)
     print(f"initial balance: {get_balance()}")   
     withdraw(500)
     print(f"Final balance: {get_balance():.2f}")
     
bank_account("Paras", 25000)          
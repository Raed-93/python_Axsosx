class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = 0

    def make_withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

    def display_user_balance(self):
        print("User: %s, Balance: %d" % (self.name, self.balance))

    def transfer_money(self, another_user, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            another_user.balance += amount
            print("Transferred: %d to %s" % (amount, another_user.name))
        else:
            print("Transfer not possible")

user1 = User("Raed", 200000)
user2 = User("Mohamad", 10000)

user1.display_user_balance()
user2.display_user_balance()

user1.transfer_money(user2, 50)
user1.display_user_balance()
user2.display_user_balance()
user1.make_withdrawal(50)


# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0
        
#     def make_deposit(self, amount):
#         self.account_balance += amount
        
#     def make_withdrawal(self,amount):
#         if self.account_balance >= amount:
#             self.account_balance -= amount
#         else:
#             print("No mony")
            
#     def display_user_balance(self):
#         print(f"User: {self.name}, Balance: ${self.account_balance}")
        
#     def transfer_money(self, other_user, amount):
#         if self.account_balance >= amount:
#             self.account_balance -= amount
#             other_user.make_deposit(amount)
#             print(f"Transferred ${amount} from {self.name} to {other_user.name}")
#         else:
#             print("Insufficient funds")

#     def __str__(self):
#         return f"User: {self.name}, Email: {self.email}, Balance: ${self.account_balance}"
    
# raed = User("Raed","email@raed")
# raed.make_deposit(200)
# raed.make_withdrawal(100)
# raed.display_user_balance()


    
          


        
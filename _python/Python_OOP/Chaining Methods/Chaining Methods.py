class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        return self

    def display_user_balance(self):
        print("User: %s, Balance: %d" % (self.name, self.balance))
        return self

    def transfer_money(self, another_user, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            another_user.balance += amount
            print("Transferred: %d to %s" % (amount, another_user.name))
        else:
            print("Transfer not possible")
        return self

# Create instances of the User class and chain method calls
user1 = User("Raed", 200000)
user2 = User("Mohamad", 10000)

user1.display_user_balance().make_withdrawal(50000).display_user_balance().transfer_money(user2, 50000).display_user_balance()
user2.display_user_balance()

# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0
        
#     def make_deposit(self,amount):
#         self.account_balance += amount
#         return self
        
#     def make_withdrawal(self, amount):
#         if self.account_balance >= amount:
#             self.account_balance -= amount
#         else:
#             print(f"Thers No {amount} in your acount ,Your Account is: {self.account_balance}")
#         return self
            
#     def display_user_balance(self):
#         print(f"User Name: {self.name}, Balance: {self.account_balance}")
#         return self
        
#     def transfer_money(self, other_user, amount):
#         if self.account_balance >= amount:
#             self.account_balance -= amount
#             other_user.make_deposit(amount)
#             print(f"Transferred ${amount} from {self.name} to {other_user.name}")
#         else:
#             print("Insufficient funds")
#         return self
        
        
# raed = User("Raed","raed@mail.com")
# ahmad = User("ahmad","ahmad@email")

# raed.make_deposit(300).make_withdrawal(100).display_user_balance().transfer_money(ahmad,30).display_user_balance()
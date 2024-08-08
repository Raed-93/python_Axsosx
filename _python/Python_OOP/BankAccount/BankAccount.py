class BankAccount:
    def __init__(self,int_rate):
        self.int_rate = int_rate
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        return self
    
    def disply_account_info(self):
        print("Account Holder: %s, Balance: %d" % (self.name,self.balance))
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
raed = BankAccount(name = "Raed",int_rate=0.02)
ahmad = BankAccount(name ="Ahmad",int_rate=0.03)

raed.deposit(1000).deposit(5000).deposit(2000).yield_interest().disply_account_info()
ahmad.deposit(5000).deposit(1000).withdraw(30000).withdraw(10000).withdraw(700).withdraw(900).yield_interest().disply_account_info()


# class BankAccount:
#     def __init__(self, int_rate=0.01, balance=0):
#         self.int_rate = int_rate
#         self.balance =balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         return self
    
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("No Many")
#             self.balance -= 5
#         return self
    
#     def display_account_info(self):
#         print(f"Balance: ${self.balance}")
#         return self
    
#     def yield_interest(self):
#         if self.balance > 0:
#             self.balance += self.balance * self.int_rate
#         return self
    

# Raed = BankAccount(int_rate=0.02, balance=100)
# Mohamad = BankAccount(int_rate=0.01, balance=200)

# Raed.deposit(150).withdraw(30).yield_interest().display_account_info()
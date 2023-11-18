class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = BankAccount(int_rate=0.02, balance=0)

    def add_account(self,account):
        self.account.append(account)

    def deposit(self,amount):
        self.balance.deposit(amount)
        return self


    def make_withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance.withdraw(amount)

    def display_user_balance(self):
        print("User: %s, Balance: %d" % (self.name, self.balance.balance))

    def transfer_money(self, another_user, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            another_user.balance += amount
            print("Transferred: %d to %s" % (amount, another_user.name))
        else:
            print("Transfer not possible")




class BankAccount:
    def __init__(self,name,int_rate):
        self.name = name
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


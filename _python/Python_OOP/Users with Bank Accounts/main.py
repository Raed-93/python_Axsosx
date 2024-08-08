class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
        
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
            
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self
        
    def transfer_money(self, other_user, amount):
        if self.account.balance >= amount:
            self.account.withdraw(amount)
            other_user.account.deposit(amount)
            print(f"Transferred ${amount} from {self.name} to {other_user.name}")
        else:
            print("Insufficient funds")
    



class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance =balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("No Many")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    
raed = User("Raed", "raed@example.com")
ahmed = User("Ahmed", "ahmed@example.com")

# إجراء عمليات على الحساب باستخدام الربط
raed.make_deposit(200).make_withdrawal(50).display_user_balance()
ahmed.make_deposit(300).make_withdrawal(100).display_user_balance()

# تحويل الأموال بين الحسابات
raed.transfer_money(ahmed, 50)
raed.display_user_balance()
ahmed.display_user_balance()


















































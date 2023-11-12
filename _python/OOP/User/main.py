class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

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


    
          


        
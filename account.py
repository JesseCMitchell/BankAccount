

class BankAccount():

    my_account_info = []

    def __init__(self, balance = 0, int_rate = 0.01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.my_account_info.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if(self.balance - amount) >0:
            self.balance -= amount
        else:
            print(f"Insufficient funds, my dude! Your balance is: {self.balance}")
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        #as long as the balance is positive, increase the account balance by the current balance, * the interest rate
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        else: 
            print("Negative balance.")
        return self


    #bonussss
    @classmethod
    def print_all_account_info(cls):
        for a in cls.my_account_info:
            print(a.display_account_info())

#first account
mikal = BankAccount(25, .01)
#second account
booker = BankAccount(1, .01)
#third account
owen_mitch = BankAccount(100, .01)

BankAccount.print_all_account_info()

mikal.deposit(500).deposit(1100).deposit(600).withdrawal(900).yield_interest().display_account_info()

booker.deposit(800).deposit(1500).withdrawal(200).withdrawal(900).withdrawal(100).withdrawal(50).yield_interest().display_account_info()

owen_mitch.deposit(10).withdrawal(500).yield_interest().display_account_info()
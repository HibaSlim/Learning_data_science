'''Create a new file called "bank_account.py"
Define the Account class and its attributes as specified above.
Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.
Define the check_balance() method. It should return the current account balance.
Create an instance of the Account class, and assign it to a variable called "my_account".
Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
Test the program by creating multiple instances of the class and performing different transactions on them.'''

class account:
    def __init__(self, account_number:str , account_balance: float, account_holder: str):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder
    def deposit(self, amount: float):
        # add amount of money to the account
        if amount >0:
            self.account_balance += amount
            print(f'deposited $ {amount}), new balance {self.account_balance}')
        else:
            print ('check the amount you want to deposit')
    def withdraw(self,amount:float):
        # withdraw money from account
        if amount >0:
            if self.account_balance>= amount:
                self.account_balance -= amount
                print(f'withdrawed $ {amount}, new balance {self.account_balance} ')
            else:
                print('insuficient balance')
        else:
            print('check the amount you want to withdraw')
    def check_balance (self):
        # check the balance of the account
        return f'your balance is: $ {self.account_balance}'

my_account = account('123456789', 5000, 'hiba')
my_account.deposit(6000)
my_account.withdraw(5220)
print(my_account.check_balance())

account1 = account('123658791', 8000, 'other')
account1.deposit(600)
account1.withdraw(10000)
print(account1.check_balance())





        



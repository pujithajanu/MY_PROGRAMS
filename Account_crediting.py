#Create an account with two attributes, balance account no. Create three methods for crediting,debiting and get the balance amount
class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def crediting(self,amount):
        self.balance+=amount
        return self.balance
    def debiting(self,amount):
        self.balance-=amount
        return self.balance
    def get_the_balance_amount(self):
        return self.balance

obj=Account(20000,25678)
print(obj.crediting(4000))
print(obj.debiting(2000))
print(obj.get_the_balance_amount())

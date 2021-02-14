'''create a bank account with members account number,name,type of account and balance.
write constructor and methods to deposit at the bank and withdraw an amount from the bank'''

#cass named bank_account
class bank_account:
    def __init__(self,name,number,Type):    #constructor is defined 
        self.acc_owner=name
        self.acc_number=number
        self.acc_type=Type
        self.balance=0
    def display(self):  #display method
        print("Owner name:",self.acc_owner)
        print("account number:",self.acc_number)
        print("type of account:",self.acc_type)
        print("balance:",self.balance)
        print()
    def deposit(self,amount):   #deposit method
        self.balance+=amount
        print("deposited amount : ",amount)
        print("Balance : ",self.balance)
        print()
    def withdraw(self,amount):  #withdraw method
        self.balance-=amount
        print("deposited amount :",amount)
        print("Balance : ",self.balance)

name=input("Enter name:")
number=int(input("enter account number :"))
Type=input("enter account type:")
amount=int(input("enter amount to deposit:"))
obj1.deposit(amount)
print()

obj1=bank_account(name,number,Type)
obj1.display()
amount=int(input("enter amount to deposit:"))
obj1.deposit(amount)
amount=int(input("enter amount to withdraw:"))
obj1.withdraw(amount)

'''output
Enter name:Meghna
enter account number :12345
enter account type:savings

Owner name: Meghna
account number: 12345
type of account: savings
balance: 0

enter amount to deposit:4000
deposited amount :  4000
Balance :  4000

enter amount to withdraw:2000
deposited amount : 2000
Balance :  2000
'''

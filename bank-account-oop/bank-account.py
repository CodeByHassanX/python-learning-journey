class bank_account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("money deposit",amount)
    def withdraw(self,amount):
        if amount >self.balance:
            print("insufficient balanace")
        else:
            self.balance -= amount
            print("money withdrawn",amount)
    def display(self):        
        print(f"Account holder: {self.name}")
        print(f"Balance: {self.balance}")

name=input("enter your name")
amount=int(input("enter your balance"))
bank=bank_account(name,amount)
while True:
    print("1.deposit")
    print("2.withdraw")
    print("3.display")
    print("4.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        amount=int(input("enter the amount to deposit"))
        bank.deposit(amount)
    elif choice==2:
        amount=int(input("enter the amount to withdraw"))
        bank.withdraw(amount)
    elif choice==3:
        bank.display()
    elif choice==4:
        break
    else:
        print("invalid choice")
class Account:
    def __init__(self, name):
        self.name=name
        self.balance=0
        
    def deposit(self, amount):
        self.balance+=amount
        return self.balance
    def withdraw(self, amount):
        if(self.balance>=amount):
            self.balance-=amount
            return self.balance
        else:
            print('{}的存款不足.'.format(self.name))
    def show(self):
        print("NT${}".format(self.balance))
userA=Account("Jack")
userA.withdraw(1000)
userA.deposit(5000)
userA.withdraw(1000)
userA.show()


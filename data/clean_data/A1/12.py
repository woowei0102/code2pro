class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount 
        print("{}存了NT${:,.0f}元".format(self.name,self.balance))     
    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
            print("{}提了NT${:,.0f}元".format(self.name,amount)) 
        else:
            print('{}的存款不足.'.format(self.name))
    def show(self):
        print("{}餘額NT${:,.0f}元".format(self.name,self.balance)) 

userA = Account("Jack") 
userA.withdraw(1000) 
userA.deposit(5000) 
userA.withdraw(1000) 
userA.show()

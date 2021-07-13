class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 1000
        
    def deposit(self, amount):
        self.balance += amount
        
        
    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            print('{}的存款不足.'.format(self.name))
            
    def show(self):
        print('{}餘額NT$'.format(self.name) + str(userA.balance))


userA = Account("Jack") 
userA.withdraw(1000) 
userA.deposit(5000) 
userA.withdraw(1000) 
userA.show()

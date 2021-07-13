class Account:
    
    def __init__(self, name):
        self.name = name
        self.balance = 0
        
    def deposit(self, amount):
        print("Jack存了NT$%d元" %amount)
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            print("Jack提了NT$%d元" %amount) 
            self.balance -= amount
        else:
            print('{}的存款不足.'.format(self.name))
    def show(self):
        print("Jack餘額NT$%d元" %self.balance)
        
userA = Account("Jack") 
userA.withdraw(1000) 
userA.deposit(5000) 
userA.withdraw(1000) 
userA.show()


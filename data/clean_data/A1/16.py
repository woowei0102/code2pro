class Account:
    def __init__(self, name):
        self.name = name
        self._balance = 0
    def deposit(self, amount):
        self._balance = self._balance + amount
        print('{}存了NT${:,.0f}元'.format(self.name,self._balance))
    def withdraw(self, amount):
        if amount < self._balance:
           self._balance = self._balance - amount
           print('{}提了NT${:,.0f}元'.format(self.name,self._balance))        
        else:
            print('{}的存款不足.'.format(self.name))
    def show(self):
        print('{}餘額NT${:,.0f}元'.format(self.name,self._balance))
userA = Account("Jack")
userA.withdraw(1000)
userA.deposit(5000)
userA.withdraw(1000)
userA.show()

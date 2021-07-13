class Account:
    def __init__(self, name):
        self.name = name
        self.__balance = 0
        
    def deposit(self, amount):
        print("{}存了NT${}元".format(self.name,amount))
        self.__balance = self.__balance + amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            print("{}提了NT${}元".format(self.name,amount))
            self.__balance = self.__balance - amount
        else:
            print('{}的存款不足'.format(self.name))
    def show(self):
        print('{}餘額NT${}元'.format(self.name,self.__balance))
userA = Account("Jack")
userA.withdraw(1000)
userA.deposit(5000)
userA.withdraw(1000)
userA.show()
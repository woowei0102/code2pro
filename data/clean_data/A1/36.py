class Account:
    def __init__(self, name):
        self.name = name
        self.__balance = 0
        
    def deposit(self, amount):
        self.__balance += amount
        print("Jack存了NT${}元".format(amount))

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Jack提了NT${}元".format(amount))
        else:
            print('{}的存款不足'.format(self.name))

    def show(self):
        print("Jack餘額NT${}元".format(self.__balance))

userA = Account("Jack")
userA.withdraw(1000)
userA.deposit(5000)
userA.withdraw(4000)
userA.show()
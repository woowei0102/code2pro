class Account:
    def __init__(self, name):
        self.name = name
        self.__balance = 0
        
    def deposit(self, amount):
        self.__balance += amount
        print("{}存了NT${}".format(self.name, amount))

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("{}提了NT${}".format(self.name, amount))
        else:
            print('{}的存款不足.'.format(self.name))

    def show(self):
        print("{}餘額NT${}".format(self.name, self.__balance))
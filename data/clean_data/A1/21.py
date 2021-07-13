class Account:
    def __init__(self, name):
        self.name = name
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount
        print(f"Jack存了NT${amount}元")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Jack提了NT${amount}元")
        else:
            print(f'{self.name}的存款不足.')

    def show(self):
        print(f"Jack餘額NT${self._balance}元")


userA = Account("Jack")
userA.withdraw(1000)
userA.deposit(5000)
userA.withdraw(1000)
userA.show()

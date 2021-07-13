

class User():  
    def __init__(self, firstName, lastName, myAge):
        self.firstName = firstName
        self.lastName = lastName
        self.__myAge = myAge-10
    def fullName(self):
        return self.firstName + "__ " + self.lastName

    def myAge(self):
        return self.__myAge

userA = User('Jack','Wu',30)
print("Hello All, My name is {}, I am {} years old.".format(userA.fullName(), userA.myAge()))

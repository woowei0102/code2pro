

class User():  
    def __init__(self, f,l,a):
        self.firstName = f
        self.lastName = l
        self._age = a
        
    def fullName(self):
        return self.firstName + " " + self.lastName

    def myAge(self):
        return self._age - 10

userA = User('Jack','Wu',30)
print("Hello All, My name is {}, I am {} years old.".format(userA.fullName(), userA.myAge()))

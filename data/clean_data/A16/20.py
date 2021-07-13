

class User():
    firstName = ""
    lastName = ""        
    __age = 0
    def __init__(self, first, last, age):
        self.firstName = first
        self.lastName = last      
        self.__age = age
    def fullName(self):
       return str(self.firstName) + " " + str(self.lastName)

    def myAge(self):
        return self.__age - 10

userA = User('Jack','Wu',30)
print("Hello All, My name is {}, I am {} years old.".format(userA.fullName(),userA.myAge()))
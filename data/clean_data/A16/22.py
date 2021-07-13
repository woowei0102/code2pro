

class User():  
    def __init__(self,name,first,age):
        self.name = name
        self.first = first
        self.__age = age
    def fullName(self):
        return self.name+ " " + self.first

    def myAge(self):
        return self.__age-10

userA = User('Jack','Wu',30)
print("Hello All, My name is {}, I am {} years old.".format(userA.fullName(),userA.myAge()))

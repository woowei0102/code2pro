class User():  
    def __init__(self, firstName,lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.__age = age

    def fullName(self):
        return self.firstName + " " + self.lastName

    def myAge(self):
        return self.__age - 10

userA = User('Jack','Wu',30)
print("Hello All, My name is "+ userA.fullName()+", I am "+str(userA.myAge()) +" years old.")
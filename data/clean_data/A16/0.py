

class User():  
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def fullName(self):
        return self.firstName + " " + self.lastName

    def myAge(self):
        self.age = self.age-10
        return self.age

userA = User('Jack','Wu',30)
print("Hello All, My name is {}, I am {} years old.".format(userA.fullName(),userA.myAge()))
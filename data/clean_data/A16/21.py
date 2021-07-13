class User():  
    def __init__(self , firstName , lastName , age):
        self.firstName = firstName
        self.lastName= lastName
        self.age = age
    def fullName(self):
        return str(self.firstName) + " " + str(self.lastName)

    def myAge(self):
        return int(self.age)

userA = User('Jack','Wu',30)
print("Hello All, My name is {}, I am {} years old.".format(userA.fullName() , userA.myAge()-10))
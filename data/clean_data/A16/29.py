

class User():  
    def __init__(self,fname,lname,age):
        self.fname,self.lname,self.__age=fname,lname,age
    def fullName(self):
        return self.fname + " " + self.lname

    def myAge(self):
        return self.__age-10

userA = User('Jack','Wu',30)
print("Hello All, My name is {0}, I am {1} years old.".format(userA.fullName(),userA.myAge()))
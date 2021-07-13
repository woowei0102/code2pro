import sys

class User():  
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.__age = age
    
    def fullName(self):
        return self.firstName + ' ' + self.lastName
    
    def myAge(self):
        return int(self.__age) - 10

if __name__ == '__main__':
    userA = User('Jack','Wu',30)
    print('Hello All, My name is {}, I am {} years old.'.format(userA.fullName(),userA.myAge()))
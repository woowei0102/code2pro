

class User():  
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age  
        
    def fullName(self):
        return self._first_name + " " + self._last_name

    def myAge(self):
        return self._age - 10

userA = User('Jack','Wu',30)
print("Hello All, My name is {}, I am {} years old.".format(userA.fullName(), userA.myAge()))

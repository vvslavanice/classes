class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.name} {self.lastname}, and i'm {self.age} years old")

user = Person('Carl', 'Johnson', 26)
user.talk()
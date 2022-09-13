class dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * dog.age_factor


somedog = dog(7)
print(f"Dog age converted to human is {somedog.human_age()}")
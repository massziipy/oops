class private:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def display(self):
        print('name=', self.name, '\n Age=', self.__age)


obj1 = private('nisham', 10)

obj1.display()

obj1.name = 'rishan'

print(obj1.name)
obj1.set_age(20)
print(obj1.get_age())

obj1.display()


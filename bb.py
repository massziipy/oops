class Parent:
    def __init__(self):
        self.__private_var = "I am private"

    def get_private(self):
        return self.__private_var


class Child(Parent):
    def access_private(self):
        # This will raise an attribute error
        print(self.__private_var)

    def access_private_with_method(self):
        # This will work fine
        print(self.get_private())


ph=Child()
ph.access_private_with_method()

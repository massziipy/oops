class Computer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return self.brand + " " + self.model


class Laptop(Computer):
    def __init__(self, brand, model, touch_screen):
        Computer.__init__(self, brand, model)
        self.touch_screen = touch_screen

    def display_info(self):
        return Computer.display_info(self) + " Touchscreen:" + str(self.touch_screen)


class GamingLaptop(Laptop):
    def __init__(self, brand, model, touch_screen, graphics_card):
        Laptop.__init__(self, brand, model, touch_screen)
        self.graphics_card = graphics_card

    def display_info(self):
        return Laptop.display_info(self) + " Graphics Card:" + self.graphics_card


computer1 = GamingLaptop("Alienware", "m15", False, "Nvidia GeForce RTX 3080")
print(computer1.display_info())

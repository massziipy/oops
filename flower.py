class Flower:
    def __init__(self, name, color, num_petals):
        self.name = name
        self.color = color
        self.num_petals = num_petals
        self.is_watered = False

    def water(self):
        if self.is_watered:
            print(self.name, "has already been watered.")
        else:
            self.is_watered = True
            print("Watering" ,self.name)

    def bloom(self):
        if self.is_watered:
            print(self.name, "is blooming.")
        else:
            print(self.name, "needs to be watered before it can bloom.")


rose = Flower("Rose", "red", 5)
rose.bloom()

rose.water()
rose.bloom()


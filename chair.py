class Chair:
    def __init__(self, num_legs, color):
        self.num_legs = num_legs
        self.color = color

    def sit_on(self):
        print("Sitting on a", self.color, "chair with", self.num_legs, "legs.")

    def repaint(self, new_color):
        self.color = new_color
        print("The chair is now", self.color)


my_chair = Chair(4, "brown")
my_chair.sit_on()
my_chair.repaint("red")
my_chair.sit_on()

class WashingMachine:
    def __init__(self, capacity):
        self.capacity = capacity
        self.detergent_level = 0
        self.water_level = 0
        self.is_on = 'OFF'

    def add_detergent(self, amount):
        self.detergent_level= self.detergent_level + amount

    def add_water(self, amount):
        self.water_level = self.water_level+ amount

    def start(self):
        if self.detergent_level > 0 and self.water_level > 0:
            self.is_on = 'ON'
            print("Washing machine started.")
        else:
            print("Cannot start washing machine. Add detergent and water.")

    def stop(self):
        self.is_on = 'OFF'
        print("Washing machine stopped.")



washingmc = WashingMachine(8)
washingmc.add_detergent(2)
washingmc.add_water(5)
washingmc.start()
# Output: Washing machine started.
washingmc.stop()
# Output: Washing machine stopped.

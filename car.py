class Car:
    def __init__(self, Name, model, year):
        self.make = Name
        self.model = model
        self.year = year
        self.speed = 0

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def accelerate(self, acceleration):
        self.speed += acceleration
        print("Car is now moving at" ,self.speed, 'mph')

    def brake(self, deceleration):
        self.speed -= deceleration
        print("Car is now moving at",self.speed, 'mph')

    def get_speed(self):
        return self.speed

my_car = Car("Verna", "Sedan", 2020)
my_car.start()
my_car.accelerate(10)
my_car.accelerate(20)
my_car.brake(5)
print(my_car.get_speed())
my_car.stop()
class Door:
    def __init__(self,model,height,width,color,material,price):
        self.color=color
        self.height=height
        self.width = width
        self.material = material
        self.price = price
        self.model = model

    def area(self):
        doorarea=self.height*self.width
        return str(doorarea)

    def details(self):
        print('model :',self.model, '\n size :',self.height,'x',self.width,'\n Material :',self.material,'\n Price :',self.price,'Rs','\n Color :',self.color)

door1 = Door('D1',10,35,'brown','wood',2000)
door1.details()
print(door1.area())




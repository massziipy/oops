class Mobile:
    def __init__(self, model, processor, display, camera, colour):
        self.model = model
        self.processor = processor
        self.display = display
        self.camera = camera
        self.colour = colour

    def power_on (self):
        print("switch on")
        print(self.camera)

    def power_off(self):
        print('switch off')

    def camera_on(self):
        print('switch on camera')


mobile1 = Mobile('s22', 'Qualcom Snapdragron gen 1', '7 inch', "13 mp", 'white')
print(mobile1.model)
mobile2 = Mobile('s23', 'Qualcom Snapdragron gen 2', '8 inch', "16 mp", 'black')
print(mobile2.model)
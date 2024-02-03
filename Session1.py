class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("MOVE")
class car(vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color = color
    def move(self):
        print("By road")
        
class boat(vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color = color
    def move(self):
        print("By Sail")
class aeroplan(vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color = color
    def move(self):
        print("Fly")

c = car("BMW","2023","red")
b = boat("speed boat","2012","White")
a = aeroplan("PIA","2000","Green and White")

for x in (c,b,a):
    print("*****************************")
    print(x.brand)
    print(x.model)
    x.move()
class vehicle:
    def move(self):
        pass




class Car(vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")




class Boat(vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("SAIL!") 


class Plane(vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Flying!") 




class Bicycle(vehicle):

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Ride!") 


Car1 = Car("Toyota","Mark X")
Boat1 = Boat("Ibiza","Touring 20")
Plane1 = Plane("Boeing","747")
Bicycle1 = Bicycle("Black","mamba")


vehicles=[Car1,Plane1,Boat1,Bicycle1]

for vehicle in vehicles:
   vehicle.move()

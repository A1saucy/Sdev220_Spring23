class Vehicle():
    def __init__(self, car, truck, plane, boat, broomstick):
        self.car = car
        self.truck = truck
        self.plane = plane
        self.boat = boat
        self.broomstick = broomstick
        
    
    
class Automobile():
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
        
    def getInfo(self, year, make, model, doors,roof,*args, **kwargs): 
        year = 2012
        make = honda
        model = civic
        doors = 4
        roof = sunroof
        
    def __repr__(self):
        return f"Your car was made in {self.year}. Your car is a {self.make} your {self.make} is a {self.model} and it has {self.doors} doors. There is a {self.roof}"   
     
class Truck(Vehicle):
    def __init__(self):
        return "Alright big shot"
    
class Plane(Vehicle):
    def __init__(self):
        return "You are part of the mile high club"
    
class Boat(Vehicle):
    def __init__(self):
        return "That's pretty swell cap"
    
class Broomstick(Vehicle):
    def __init__(self):
        return "You scary"
        
ride = Automobile(2012, "honda", "civic", 4,"sunroof")
print(ride)

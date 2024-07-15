
traffic_light = "Green"

speed_limit = 60

class Vehicle:
    def start_engine(self):
        message = "Engine started."
        print(message)

# Derived class 1
class Car(Vehicle):
    def __init__(self, make):
        self.make = make

    def start_engine(self):
        message = "Car engine started."
        print(message)

# derived class 2
class Bike(Vehicle):
    def __init__(self, bike_type):
        self.type = bike_type

    def start_engine(self):
        message = "Bike engine started."
        print(message)

#Main Function
def main():
    print("Global variable traffic_light:", traffic_light)
    print("Module variable speed_limit:", speed_limit)
    
    my_car = Car("Nano")
    my_bike = Bike("Mountain")
    
    print("Car make:", my_car.make)
    print("Bike type:", my_bike.type)
    
    vehicles = [my_car, my_bike]
    for vehicle in vehicles:
        vehicle.start_engine()

if __name__ == "__main__":
    main()

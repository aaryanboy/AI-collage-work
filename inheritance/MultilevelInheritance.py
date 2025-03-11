class Vehicle:
    def show(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class SportsCar(Car):
    def race(self):
        print("SportsCar is racing.")



s = SportsCar()
s.show()  
s.drive() 
s.race()


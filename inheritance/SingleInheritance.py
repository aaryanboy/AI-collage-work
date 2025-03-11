class Vehicle:
    def show(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

c = Car()
c.show()  # Inherited method
c.drive()

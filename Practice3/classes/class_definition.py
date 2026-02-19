class Car:
    wheels = 4   # class variable (shared by all cars)

    def __init__(self, brand, speed):
        self.brand = brand    # instance variable
        self.speed = speed    # instance variable

    def drive(self):
        print(self.brand, "is driving at", self.speed, "km/h")
c1 = Car("Toyota", 120)
c2 = Car("BMW", 200)

c1.drive()
c2.drive()

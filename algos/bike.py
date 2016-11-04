class bike(object):
    def __init__(self,price=200):
        self.price = price
        self.maxSpeed= '25mph'
        self.mileage =0
    def reverse(self,hours):
        self.mileage -= (5 * hours)
        if self.mileage<0:
            self.mileage=0
    def ride(self,hours):
        print "Riding..."
        self.mileage += (10 * hours)
    def displayInfo(self):
        print "Price:",self.price
        print "Max Speed:",self.maxSpeed
        print "Mileage:",self.mileage
bike1 = bike(350)
bike2 = bike(185)
bike3 = bike()
print bike1, bike2, bike3
bike1.displayInfo()
bike1.ride(3)
bike1.reverse(1)
bike1.displayInfo()
bike2.ride(2)
bike2.reverse(2)
bike2.displayInfo()
bike3.reverse(3)
bike3.displayInfo()

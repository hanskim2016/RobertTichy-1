class car(object):
    def __init__(self,speed,fuel,mileage,price=2000):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax()
    def display_all(self):
        print "Price:",self.price
        print "Speed:",self.speed
        print "Fuel:",self.fuel
        print "Taxed at:",self.taxrate
        print "Tax:",self.tax
        return self
    def tax(self):
        if self.price>10000:
            self.taxrate=.15
        else:
            self.taxrate=.12
        self.tax = self.taxrate * self.price
a = car(55,"Full",3325,8500)
b = car(55,"Full",8325,18500)
c = car(55,"Full",33225,38500)
d = car(55,"Full",34325,68500)
e = car(55,"Full",33325,128500)

a.display_all()
b.display_all()
c.display_all()
d.display_all()
e.display_all()
f = car(65,"Half",0)
f.display_all().display_all()

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = (self.price/100)*15
        else:
            self.tax = (self.price/100)*12
        self.display_all()
    def display_all(self):
        print "\n"
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + self.fuel
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax)

car1 = Car(2000, 35, "Full", 23)
car2 = Car(5000, 60, "Quarter full", 18)
car3 = Car(7500, 55, "Empty", 15)
car4 = Car(11300, 45, "3/4 full", 27)
car5 = Car(3400, 10, "Empty", 13)
car6 = Car(25999, 0, "Half tank", 32)

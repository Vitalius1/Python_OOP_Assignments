class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "This bike costs $" + str(self.price) + " and has a maximum speed of " + str(self.max_speed) + ". It has " + str(self.miles) + " miles on the board."
    
    def ride(self):
        print "Riding..."
        self.miles += 10
        return self
    
    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(250, 100)
bike2 = Bike(325, 130)
bike3 = Bike(400, 150)
print bike1.displayInfo()
print bike2.displayInfo()
print bike3.displayInfo()

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
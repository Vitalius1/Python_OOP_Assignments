class Product(object):
    def __init__(self, item_name, brand, weight, cost):
        self.item_name = item_name
        self.brand = brand
        self.price = 0
        self.weight = weight
        self.cost = cost
        self.status = "for sale"
    def display_info(self):
        print "Product name: " + self.item_name + "."
        print "it's of " + self.brand + " brand."
        print "The price including sales tax is $" + str(self.price)
        print "It weights " + str(self.weight) + " lbs."
        print "It's cost is: $" + str(self.cost) + "."
        print "Status: " + self.status

    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        self.price = self.cost +(self.cost/100) * tax
        return self
    
    def return_product(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.cost = 0
        elif reason == "changed mind":
            self.status = "for sale"
        elif reason == "open box":
            self.cost = self.cost - (self.cost/100) * 20
            self.status = "used"
        else:
            self.cost = self.cost - (self.cost/100) * 50
            self.status = "used"

        return self

book = Product('Wikipedia', 'dictionary', 2, 50.00)
book.add_tax(9.5).sell().return_product("didn't like it").add_tax(9.5).display_info()
class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "The " + self.name + "'s health is " + str(self.health)

anim1 = Animal("dog")
anim1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

anim2 = Dog("Alfa")
anim2.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print "I am a Dragon"
        super(Dragon, self).display_health()

anim3 = Dragon("Drago")
anim3.walk().walk().run().run().fly().fly().display_health() 
# anim3.walk().walk().run().run().pet().fly().fly().display_health()  #this should not work cause dragon subclass has no method pet
anim4 = Animal("Elephant")
anim4.walk().run().display_health()
# anim4.pet().display_health()  # It's not working cause Animal class has no method pet
# anim4.fly().display_health()  # It's not working cause Animal class has no method fly
# anim2.fly().display_health()  # It's not working cause Dog subclass has no method fly
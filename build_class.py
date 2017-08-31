class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    def login(self):
        self.logged = True
        print self.name  + " is logged in."
        return self

user1 = User('Diana', 'dia@gmail.com')
user2 = User('Vitalie', 'vit@yandex.com')
print user1.name, user1.email, user1.logged
print user2.name, user2.email, user2.logged

print user1.login()
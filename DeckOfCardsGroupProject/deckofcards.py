import random

cardarray = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ["\xe2\x99\xa5", "\xe2\x99\xa0", "\xe2\x99\xa3", "\xe2\x99\xa6"]


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def printcard(self):
        temp = ''
        if self.value <= 10:
            temp = self.value
        if self.value == 11:
            temp = 'Jack'
        if self.value == 12:
            temp = 'Queen'
        if self.value == 13:
            temp = 'King'
        if self.value == 14:
            temp = 'Ace'
        print "{} {}".format(self.value, self.suit)


class Deck(object):
    def __init__(self):
        self.deckcards = []
        for s in suits:
            for i in cardarray:
                self.deckcards.append(Card(s, i))
        self.decklength = len(self.deckcards)

    def shuffle(self):
        for i in range(self.decklength - 1):
            idx = random.randint(0, self.decklength - 1)
            temp = self.deckcards[i]
            self.deckcards[i] = self.deckcards[idx]
            self.deckcards[idx] = temp
        return self

    def draw(self):
        yourdraw = self.deckcards.pop()
        self.decklength -= 1
        return yourdraw

    def remove(self):
        yourdraw = self.deckcards.pop()
        self.decklength -= 1 
        return self       

    def addcard(self, card_to_add):
        for i in range(len(self.deckcards) - 1, -1, -1):
            self.deckcards[i] = self.deckcards[i - 1]
        self.deckcards[0] = card_to_add
        self.decklength += 1
        return self

    def printdeck(self):
		print "The Deck of Cards is shuffled..."
		for c in self.deckcards:
			c.printcard()


class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name

    def receive(self, deck):
        temp = deck.draw()
        self.hand.append(temp)
        return self

    def giveI(self, deckRef, idx):
        if idx > len(self.hand) - 1:
            idx = len(self.hand) - 1
        swap = self.hand[idx]
        self.hand[idx] = self.hand[len(self.hand) - 1]
        self.hand[len(self.hand) - 1] = swap
        self.hand.pop()
        deckRef.addcard(swap)
        return self
    def showhand(self):
        for card in self.hand:
	       card.printcard()
        return self


class Table(object):
    def __init__(self):
        self.tabletop = []
        self.p1score = 0
        self.p2score = 0
        self.points = 1
    def addcard(self, card_to_add):
        self.tabletop.append(card_to_add)
        return self
    def compare(self, deck, p1, p2):
        for card in self.tabletop:
            string = ''
            string += str(card.suit)
            string += str(card.value)
            print string
        for card in self.tabletop:
            if len(self.tabletop) != 2:
                print "Table has: " + str(len(self.tabletop))
                break
            elif self.tabletop[0].value > self.tabletop[1].value: 
                self.p1score += self.points
                self.points = 1
                break
            elif self.tabletop[0].value < self.tabletop[1].value:
                self.p2score += self.points
                self.points = 1
                break
            elif self.tabletop[0].value == self.tabletop[1].value:
                deck.remove().remove().remove()
                self.points += 3
                break
        print p1.name + " score: " + str(self.p1score)
        print p2.name + " score: " + str(self.p2score)
        self.tabletop = []
        return self


aDeck = Deck().shuffle()
aDeck.printdeck()
aPlayer = Player('Vitali')
bPlayer = Player('Brandon')
t = Table()

print ''
print "5 CARD WAR!"
print ''
aPlayer.receive(aDeck).receive(aDeck).receive(aDeck).receive(aDeck).receive(aDeck).giveI(t, len(aPlayer.hand))
bPlayer.receive(aDeck).receive(aDeck).receive(aDeck).receive(aDeck).receive(aDeck).giveI(t, len(bPlayer.hand))
t.compare(aDeck, aPlayer, bPlayer)
print ''
aPlayer.giveI(t, len(aPlayer.hand))
bPlayer.giveI(t, len(bPlayer.hand))
t.compare(aDeck, aPlayer, bPlayer)
print ''
aPlayer.giveI(t, len(aPlayer.hand))
bPlayer.giveI(t, len(bPlayer.hand))
t.compare(aDeck, aPlayer, bPlayer)
print ''
aPlayer.giveI(t, len(aPlayer.hand))
bPlayer.giveI(t, len(bPlayer.hand))
t.compare(aDeck, aPlayer, bPlayer)
print ''
aPlayer.giveI(t, len(aPlayer.hand))
bPlayer.giveI(t, len(bPlayer.hand))
t.compare(aDeck, aPlayer, bPlayer)
print ''

import random

cardarray = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
suits = ["\xe2\x99\xa5", "\xe2\x99\xa0", "\xe2\x99\xa3", "\xe2\x99\xa6"]


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def printcard(self):
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
        # print len(self.hand)
        return self

    def giveI(self, deckRef, idx):
        if idx > len(self.hand) - 1:
            idx = len(self.hand) - 1
        swap = self.hand[idx]
        self.hand[idx] = self.hand[len(self.hand) - 1]
        self.hand[len(self.hand) - 1] = swap
        self.hand.pop()
        deckRef.addcard(swap)
        # print len(self.hand)
        return self

    def showhand(self):
		print "The player has in his hand {} cards.".format(len(self.hand))
		for card in self.hand:
			print list(card.printcard())



aDeck = Deck().shuffle()
aPlayer = Player('Vitali')
aDeck.printdeck()
# aPlayer.showhand(aDeck).giveI(aDeck, 2).showhand(aDeck)
aPlayer.receive(aDeck).receive(aDeck).showhand()

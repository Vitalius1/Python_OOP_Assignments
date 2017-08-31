class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.deal())
        return self
    
    def discard(self, index):
        return self.hand.pop(index)
    
    def show_hand(self):
        print
        print "{} has {} cards.".format(self.name, len(self.hand)),
        for card in self.hand:
             print card.value, card.suit, " ~ ",
        print
        print "_________________________________________________"
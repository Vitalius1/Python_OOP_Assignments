from my_card import Card
import random
class Deck(object):
    def __init__(self):
        suits = ["\xe2\x99\xa5", "\xe2\x99\xa0", "\xe2\x99\xa3", "\xe2\x99\xa6"]  # using this to display suits in terminal
        values = [2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King', 'Ace']
        self.my_deck = []
        for v in values:
            for s in suits:
                self.my_deck.append(Card(v, s))
    
    def deal(self):
        return self.my_deck.pop()
    
    def shuffle(self):
        for x in range(len(self.my_deck)):
            rand = random.randint(0,51) 
            temp = self.my_deck[x]
            self.my_deck[x] = self.my_deck[rand]
            self.my_deck[rand] = temp

    def show_deck(self):
        print
        print "_________________THE DECK__________________"
        print
        for card in self.my_deck:
            print card.value, card.suit, " ~ ",
        print
        print
        print "-------------The deck has " + str(len(self.my_deck)) + " cards.-------------"
        print
        print "=========================================================="
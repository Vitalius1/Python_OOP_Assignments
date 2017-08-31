from my_deck import Deck
from my_card import Card
from my_player import Player

deck1 = Deck()
deck1.shuffle()
# deck1.show_deck()
player1 = Player("Vitalie")
player1.draw(deck1).draw(deck1).draw(deck1).draw(deck1).draw(deck1)
deck1.show_deck()
player1.show_hand()

deck1.my_deck.insert(0, player1.discard(0))
deck1.show_deck()
player1.show_hand()

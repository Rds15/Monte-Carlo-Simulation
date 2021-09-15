from Card import Card
from Deck import Deck
 
class Hand:
    def __init__(self) -> None:
        self.hand = []

    def fill_hand(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()        
             
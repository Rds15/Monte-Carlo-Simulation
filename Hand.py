from Card import Card
from Deck import Deck
 
class Hand(Card):
    def __init__(self) -> None:
        self.hand = []
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def fill_hand(self, deck):
        #fill hand with 13 cards
        for i in range(13):
            self.hand.append(deck.drawCard())

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #output hand
    def showHand(self):
        for card in self.hand:
            card.show()
        
        #for clarity
        print('')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #output length of hand
    def len_hand(self):
        return len(self.hand)
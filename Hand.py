from Card import Card
from Deck import Deck
 
class Hand(Deck):
    def __init__(self) -> None:
        self.hand = []

    #def fill_hand(self):
        #fill should take t
        for s in range(14):
            for v in range(14):
                self.hand.append(Card(s,v))

    def show(self):
        for h in self.hand:
            h.show()
        
        print({})                    
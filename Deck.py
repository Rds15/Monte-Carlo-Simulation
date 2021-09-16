from Card import Card
import random

class Deck:

    def __init__(self) -> None:
        self.cards = [] #array
        self.build() #function
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def build(self):
        #adding integers
        for s in ['S','C','D','H']:                        
            for v in range(2,11): #integers 1-10
                self.cards.append(Card(s,v))
        
        #adding faces
        for s in ['S','C','D','H']:
            for v in ['K','Q','J','A']:
                self.cards.append(Card(s,v))
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def shuffle(self):
        return random.shuffle(self.cards)


    #test output
    def show(self):
        for c in self.cards:
            c.show()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def drawCard(self):
        
        return self.cards.pop(0)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #output length (for testing)
    def show_len(self):
        return len(self.cards)
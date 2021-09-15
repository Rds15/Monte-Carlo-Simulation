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
        #start at last index, end at first, decrement by 1
        for i in range(len(self.cards) -1, 0, -1):

            rand = random.randint(0,i) # random number between 1-51

            #swap card 'i' and randomly chosen number card 'rand'
            self.cards[i],self.cards[rand] = self.cards[rand], self.cards[i]


    #test output
    def show(self):
        for c in self.cards:
            c.show()
        
        print({})

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    def get_card(self):
        return self.cards.index('10')

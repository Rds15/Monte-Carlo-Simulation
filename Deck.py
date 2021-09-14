from Card import Card

class Deck:

    def __init__(self) -> None:
        self.cards = [] #array
        self.build() #function
    
    def build(self):
        #adding integers
        for s in ['S','C','D','H']:
            for v in range(2,11): #integers 1-10
                self.cards.append(Card(s,v))
        
        #adding faces
        for s in ['S','C','D','H']:
            for v in ['K','Q','J','A']:
                self.cards.append(Card(s,v))

    #test output
    def show(self):
        for c in self.cards:
            c.show()
        
        print({})
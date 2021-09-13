
class Card:

    #
    def __init__(self,suit,val) -> None:
        self.suit = suit
        self.value = val
    
    #test output
    def show(self):
        print("{} of {}".format(self.value, self.suit))
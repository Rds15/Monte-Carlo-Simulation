
class Card:
    def __init__(self,suit,val) -> None:
        self.suit = suit
        self.value = val
    def show(self):
        print("{} of {}").__format__(self.value, self.suit)
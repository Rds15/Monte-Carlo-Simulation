                                                                                                                                                                                                                                                                                              
class Card:

    #
    def __init__(self,suit,val) -> None:
        self.suit = suit
        self.value = val
    
    #test output
    def show(self):
        print("{}{}".format(self.value, self.suit), end=" ")

    def get_val(self):
         print(self.value)

    def get_suit(self):
        return self.suit
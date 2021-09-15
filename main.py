from Card import Card
from Deck import Deck
from Hand import Hand
from array import *


def main():

    deck = Deck()
    deck.shuffle()
    deck.show()
    
    print('Here is a returned card: {}'.format(deck.get_card()))


main()
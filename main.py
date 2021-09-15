from Card import Card
from Deck import Deck
from Hand import Hand
from array import *


def main():

    deck = Deck()
    deck.shuffle()
    deck.show()

    hand = Hand()
    hand.fill_hand(deck)
    hand.showHand()
   


main()
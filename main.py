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
    hand.fill_hand(deck)
    hand.showHand()

    print('\nlength: {}\n\n'.format(deck.show_len()))

    deck.show()


main()
from Card import Card
from Deck import Deck
from Hand import Hand
from array import *


def main():

    deck = Deck()
    deck.shuffle()
   # deck.show()

    hand = Hand()
    hand.fill_hand(deck)
    hand.showHand()

    print('\nlength: {}'.format(deck.show_len()))
    print('length of hand: {}\n'.format(hand.len_hand()))


main()
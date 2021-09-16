from Card import Card
from Deck import Deck
from Hand import Hand
from array import *


def main():
    card = Card('','')

    deck = Deck()
    deck.shuffle()

    hand = Hand()
    hand.fill_hand(deck)

    print('\nHere is your Hand:')
    hand.showHand()
    #get size of hand and deck (testing)
    #print('\nlength: {}'.format(deck.show_len()))
    #print('length of hand: {}\n'.format(hand.len_hand()))
main()
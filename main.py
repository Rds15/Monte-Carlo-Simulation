from Card import Card
from Deck import Deck
from Hand import Hand
from array import *


def main():
    card = Card('','')

    deck = Deck()
    deck.shuffle()
   # deck.show()

    hand = Hand()
    hand.fill_hand(deck)
    hand.showHand()

    print('\n\n')
    hand.calculate(card)
    
    
    #get size of hand and deck (testing)
    print('\nlength: {}'.format(deck.show_len()))
    print('length of hand: {}\n'.format(hand.len_hand()))
main()
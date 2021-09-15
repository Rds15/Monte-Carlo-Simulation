from Card import Card
from Deck import Deck


def main():

    card = Card("Card",6)
    card.show()

    deck = Deck()
    deck.show() # print ordered deck
    deck.shuffle() #shuffle
    print('\n\n')
    deck.show() # print shuffled deck

main()
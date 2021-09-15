from Card import Card
from Deck import Deck


def main():

    card = Card("Card",6)
    card.show()

    deck = Deck()
    deck.show()
    deck.shuffle()
    print('\n\n')
    deck.show()

main()
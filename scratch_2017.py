#warmup dec 13
from itertools import product
deck = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}
sign = ["Diamonds","Spades","Hearts","Clubs"]
class card_in_deck():
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value
# cards_tuples = list(product(deck, sign))
card_format = "{} of {}".format(cards_tuples)
    def new_card(self):
        for i in deck:
            for k in sign:
                return new_card



print(card_in_deck(new_card))
# print(cards_tuples)






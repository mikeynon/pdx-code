#warmup dec 13
import random
import time
# cards_deck = 'Ace'* 4,'2'* 4,'3'* 4,'4'* 4,'5'* 4,'6'* 4,'7'* 4,'8'* 4,'9'* 4,'10'*4,'Jack'* 4,'King'* 4,'Queen'* 4
card_values = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'King': 10,
    'Queen': 10
}

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{} of {}'.format(self.rank, self.suit)

#
deck = []

for s in suits:
    for rank, value in card_values.items():
        deck.append(Card(s, rank, value))
random.shuffle(deck)
dealer_hand = [deck[0], deck[1]]
my_hand = [deck[2], deck[3]]

print("shuffling")
time.sleep(2)
print("Dealer has "+ str(dealer_hand))
print("dealing")
time.sleep(1)
print("My cards are "+ str(my_hand))
while True:
    user_move = input("Would you like to stay or hit?:\n")
    if user_move in "hit":
        hit = my_hand.append(deck[])
        print(my_hand)
        True
    elif user_move in "stay":
        print(my_hand)
        break
else:
    print(my_hand)
def eval_hand(dealer_hand):
    for i in dealer_hand[0][1]:
        value = int(i)
        if i in "A":
            if eval_hand > 21:
                value == 1
            elif eval_hand <= 21:
                value == 11

 def eval_hand(my_hand):
    for i in my_hand[0][1]:
        value = int(i)
        if i in "A":
            if eval_hand > 21:
                value == 1
            elif eval_hand <= 21:
                value == 11


eval_hand(my_hand)
eval_hand(dealer_hand)

def winning():
    if 21 >= my_handprint > dealer_hand:
        print("You Win")
    elif 21 >= dealer_hand > my_hand:
        print("You Lose")
    elif my_hand > 21:
        print("You Lose")
    else:
        print("Draw")
print(winning)

#
# def counth(hand):
#     count = 0
#     for i in hand:
#         if i in values:
#             count += values[i]
#         else:
#             pass
#     for x in hand:
#         if x == 'A':
#             if count + 11 > 21:
#                 count += 1
#             elif hand.count('A') == 1:
#                 count += 11
#             else:
#                 count += 1
#         else:
#             pass
#     return count
# print(hand)
# print(count)






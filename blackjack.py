import random
# suits = ("Clubs", "Hearts", "Spades", "Diamonds")
facevalue = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "Jack":10, "Queen":10, "King":10}
# # dealer_hand = random.choice(deck_dic(random.randint, random.randint))
#
# print (random.choice(suits))
#
# # def hand_hit(empty_hand):
# #     hands = int({}{}+{}{}) if x <= 21:
# #     while True:
# #         if your_hand == 21:
# #             print("blackjack")
# #         elif your hand_hands_hand < 21:
# #             return(hand_hit(hands))
# #         if either_hand > 21:
# #             lose
# #         else:
# #
# #
# # draw = dealer_hand + your_hand
# #
# # while draw != 21
# #     return(hit_hand(your_hand))
# #
# # if card selected, pop from key and dictionary
# # if __name__ = '__main__':
# #     print()##################################
user_hand = input("Type in your first card(just value or face, no suits):\n")
def hand_value(user_hand):
    for user_hand in facevalue:
        return(facevalue(user_hand).value())



print(hand_value(user_hand))
# if user_hand == 21:
#     print("Blackjack!")
# elif user_hand <= 15:
#     print("Hit!")
# elif user_hand > 15:
#     print("Stay!")
# else:
#     print("you lose")
if __name__ == "__main__":
    import doctest
    doctest.testmod()

PIG LATIN

LAB: PIG LATIN
DELIVERY METHOD: PROMPT ONLY
GOAL
Create a program asks for a single English word and translates it to Pig Latin.
It prints out the input word and the resulting translation like the example below.

INSTRUCTIONS
If the first letter is a consonant, move it to the end.
Add “ay” to the end of that.
If the first letter is a vowel, just ad “yay” to the end.


import time
print("\n\nWelcome to Pig Latin Rosetta Stone!\n\n\n")
user_word = input("Please type word that you would like translated:\n")
print("translating now...")
time.sleep(2)
moving_item = user_word.strip(user_word [0][-1]) + user_word[0][0] + "ay."
 # " +user_word[1][1:90], + user_word[1][0] + "ay "user_word[2][1:90], + user_word[2][0] + "ay "user_word[3][1:90], + user_word[3][0] + "ay "user_word[4][1:90], + user_word[4][0] + "ay.")

if moving_item[0] is "b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "v" or "w" or "x" or "y" or "z":
    print(moving_item)
else:
    print("That doesnt work, bro.")

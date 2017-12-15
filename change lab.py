CHANGE RETURN

LAB: CHANGE RETURN
DELIVERY METHOD: DOCTESTS
GOAL
Write a python script that figures out how to divvy up an amount of change into the fewest quarters, dimes, nickels, and pennies.

INSTRUCTIONS
Some supermarkets have automatic change dispensers.

Ask for the amount of change to dispense in cents.
Assume that the amount input will be less than 100 cents.
Calculate the number of quarters necessary first.
Then calculate the number of dimes, nickels, and pennies.
If you do it in that order, you will minimize the number of coins.
This is easiest done by updating a running total of number of cents left to be put into coins.

Also remember that the // operator divides and removes any remainder.

DOCUMENTATION
PYTHON OFFICIAL DOCS: OPERATORS
ADVANCED
Expand this problem to work on an amount of cents greater than 100 and include bills.
Print out the total number of coins and bills dispensed.
SUPER ADVANCED
Store how many of each coin is in the cash register, then allow the change algorithm to deal with when you don’t have enough coins to optimally give change.
KEY CONCEPTS
Operators
Variables
Data Types
PEP8
"""
>>> make_change(94)
3 quarters
1 dimes
1 nickles
4 pennies
>>> make_change(75)
3 quarters
>>> make_change(42)
1 quarters
1 dimes
1 nickles
2 pennies
"""


initial_money = float(input("You need change? How much you got?\n:")) * 100
coin_choice = input("I can break that for you, for a small fee. What type of coins do you want?\n:")
if coin_choice == "pennies":
    pennies_bin = initial_money // 100
    print("That's exactly" + str(pennies_bin) + " pennies. You're a pain in the ass.")
if coin_choice == "nickels":
    nickels_bin = int(initial_money // 5)
    change_bin = int(initial_money%5)
    print("That's " + str(nickels_bin) + " nickels. That means there's " + str(change_bin) + " cents left over.")
if coin_choice == "dimes":
    dimes_bin = int(initial_money // 10)
    change_bin2 = int(initial_money%10)
    print("That's " + str(dimes_bin) + " dimes. That means there's " + str(change_bin2) + " cents leftover.")
if coin_choice == "quarters":
    quarters_bin = int(initial_money // 25)
    change_bin3 = int(initial_money%25)
    print("That's " + str(quarters_bin) + " quarters. That means there's " + str(change_bin3) + " cents leftover.")
coin_toss = ["heads", "tails"]
second_question = input("Do you want to make a bet with those leftover cents?\n:")
if second_question == "yes":
    print("Ill flip a coin. If it comes up heads, you keep the change. If it comes up tails, I keep the change.")
if second_question == "no":
    print("Okay, fine then.")

# Write your code below.

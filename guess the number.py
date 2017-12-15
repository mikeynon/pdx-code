import random
import time
trys = 0
print("\n\nWelcome to the Guessing Game!\n")
user_guess = int(input("Guess how many fingers I'm holding up:\n"))
comp_num = random.randint(0,10)
while trys < 3:
    user_guesses = trys + 1
    trys = int(user_guesses) + 1
    if user_guess < comp_num:
        print("lemme count")
        time.sleep(1)
        print("too low!")
        user_guesses = trys + 1
    if user_guess > comp_num:
        print("lemme count")
        time.sleep(1)
        print("too high!")
        user_guesses = trys + 1
    if user_guess == comp_num:
        break
if trys == int(user_guesses):
    print("thats all the trys you get.")
elif user_guess == comp_num:
    print("lemme count")
    time.sleep(1)
    print("you guessed right!")
else:
    print("I only got ten fingers.")

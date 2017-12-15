import random

user_in = input("What message would you like to anagram?:\n")

l = list(user_in)
random.shuffle(l)
result = ''.join(l)
print(result)

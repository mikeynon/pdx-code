# """
# WORD COUNT
#
# LAB: WORD COUNT
# DELIVERY METHOD: PROMPT ONLY
# GOAL
# Write a python module to analyze a given text file containing a book for is vocabulary frequency and display the most frequent words to the user in the terminal.
#
# INSTRUCTIONS
# Find a book on Project Gutenberg.
# Download it as a UTF-8 text file.
#
# Open the file and deal with any decoding errror that arise.
# Normalize all of the words so differences in capitalization and punctuation attached to words don’t affect the counts.
# Count how often each unique word is used, then print the most frequent top 10 out with their counts.
# """
#
#     """
#     WORD Counter
#     """
from collections import Counter
ctr = Counter()
token_ctr = 0
with open('FLWRSFTHSKY.txt', 'r') as f:
    for line in f:
       line_words = line.strip().split()
       for word in line_words:
           if len(word) > 4:
               token_ctr += 1
               ctr[word] += 1

def mostcommon():
    print("The most common words are ", ctr.most_common(10))
    print("There are ",token_ctr, " words in 'Flowers of the Sky' by Proctor.")
    print("There are ",len(ctr), " unique words therein.")
print(mostcommon())
user_file = input("Please upload your text to be analyzed:\n")

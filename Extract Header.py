EXTRACT HEADER

LAB: EXTRACT HEADER
DELIVERY METHOD: DOCTESTS
GOAL
Write a python function to parse a string containing email address data for the first matching domain name.
Exaple: chris@pdxcodeguild.com should print as “pdxcodeguild”.

import time
sep = "@"
url = "."
email_in = input("Simplify your email to find out the host:\n")
print("Your host is...")
time.sleep(2)
print(email_in.lstrip(sep))

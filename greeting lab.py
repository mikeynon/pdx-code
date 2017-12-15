import datetime
import time
from datetime import date


name1 = input("please input your name:\n")
age1 = input("please input your birthday (YYYY/MM/DD):\n")
age = date.today() - time.strptime(age1)
print(age.days)
print("Hello, " + name1 +", nice to see you!  You are " + (age) + " days old.")

# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
cc_num = []
import time
def cc_break(initial):
    first = initial[:3]
    second = initial[4:7]
    third = initial[8:11]
    last = initial[12:]
    print("{}-{}-{}-{}").format(first, second, third, last)
    return
def cc_company(cc_break):
    if cc_break(last).length() == 4:
        print("This looks like a mastercard or visa")
    elif cc_break(last).length() == 3:
        print("This looks like an american express")
check_num = initial[-1]
def dbl_math(math_num):
    for i in math_num:
        return (i * 2)
def find_nines(dbl_math):
    if i in dbl_math > 9:
        return (i - 9)
    else:
        return i
def last_two(find_nines):
    sum[find_nines]

initial = input("Please type your credit card number to be verified:\n")
print(cc_company, cc_break)
list_num = check_num.split()
math_num = list_num.reverse()
print(cc_company, cc_break)
print("Verifying")
time.sleep(3)

if str(last_two[-1]) == check_num:
    print("This card is real!")
else:
    print("This is not a valid card.")

from operator import mul
import functools
list_1 = [0,1,2,3,4]
def merge_1(num, mult):
    if num<=0:
        returnmul(num, mult)
print(list(map(functools.partial(mul, 2), list_1)))

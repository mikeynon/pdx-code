
number_list = (range(0,100))
def list1():
    for i in number_list:
        if ((i%3==0) and (i%5==0)):
                print("fizzbuzz")
        elif (i%3==0):
            print("fizz")
        elif (i%5==0):
            print("buzz")
        else:
            print(i)
def List2():
    for i in number_list:
        if "fizzbuzz":
            if ((i-1)%2==0) and ((i+1)%6==0):
                print(i)
        elif "fizz":
            ((i-1)%2==0)
            print((i-1))
        elif "buzz":
            ((i+1)%6==0)
            print(i+1)
        else:
            print("Not divisible by 3 or 5")

print(list1(List2))

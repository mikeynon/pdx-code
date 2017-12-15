import time

def shrink(unshrunk):
    print("18953543609845982435098249999999999999999999999999999999999999999999999999958452450517")
    num_list = [int(x) for x in list(unshrunk) if x.isdigit()]
    while True:
        if len(num_list) == 1:
            return num_list[0]
        else:
            num_list = [int(x) for x in str(sum(num_list))]
        

# def shrink_recursive(unshrunk):
#     num_list = [int(x) for x in list(unshrunk) if x.isdigit()]
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         num_list = str(sum(num_list))
#         return shrink_recursive(num_list)

if __name__ == '__main__':

    print(shrink('18953543609845982435098249999999999999999999999999999999999999999999999999958452450517'))
    # print(shrink_recursive('1895354360517'))

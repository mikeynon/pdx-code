
height_1 = int(input("Whats the height, in feet, of the wall you want to paint?:\n"))
width_1 = int(input("Whats the width, in feet, of that wall?:\n"))
paint_price = int(input("How much is a gallon of paint?:\n$"))
coats_1 = int(input("How many coats will you need to apply?:\n"))
surf_area = height_1 * width_1 * coats_1
paint_coats = math.ceil(surf_area / 400)
cost = paint_coats * paint_price
print("Well, Its gonna cost $" + str(cost) + " for " + str(paint_coats) + " buckets of paint.")

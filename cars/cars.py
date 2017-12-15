# CREATE A CLASS
#
# LAB: CREATE A CLASS
# OBJECTIVE
#
# Create a Car class with some attributes typical of automobiles, then use it to create some instances of different cars.
#
# Create a new directory called cars
# Create the following 2 files inside the cars directory: main.py and car.py
# In car.py, create a class called Car with the following characteristics:
# A shared property called number_of_wheels set to the value 4
# The following instance properties that get set upon initialization:
# color
# number_of_doors
# A honk method that, when called, prints out the word honk
# In main.py, import your Car class and create 2 or 3 instances of cars with different characteristics; when you run main.py it should print out the characteristics of your Car instances
import random
color_list = ["red","beige", "black"]
colors = random.choice(color_list)
door_amounts = [1,2,3,4,5]
number_of_doors = random.choice(door_amounts)

class car:
    def __init__(self, color, number_of_doors):
        self.color = color
        self.number_of_doors = number_of_doors
        number_of_wheels = 4

    def color(self):
        print("The car is {}.".format.self.color)

    def number_of_doors(self):
        print("It has {} doors.".format.self.number_of_doors)

    def honk(self):
        print("HONK")

car_1 = car("Mikes Car: ")
print(car_1)

# if __name__ == "__main__":

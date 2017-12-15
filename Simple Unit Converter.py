# SIMPLE UNIT CONVERTER
#
# LAB: SIMPLE UNIT CONVERTER
# OBJECTIVE
#
# Write a simple program that, when run, prompts the user for a number of miles,
# then prints the equivalent number of feet.
#
# Open Atom
# Create a new file and save it as simpleunitconvert.py
# Implement the program, ideally without peeking at the solution

travel_dict = {"walking":1, "running":2, "biking":3, "driving":4, "flying":5}
distance = float(input("How many miles are you going?\n:"))
traveling = input("Thats not too far. How are you traveling?\n:")
if 'walk' in traveling:
    miles_rate = int(distance) // 3
    print("That should take about " + str(miles_rate) + " hours.")
    change_unit = input("Do you want to change the speed?\n:")
    if 'y' in change_unit:
        new_rate = float(input("How many miles per hour will you travel?\n:"))
        time = int(distance) / int(new_rate)
        print("Then your trip would take you " + str(time) + " hours at " + str(new_rate) + "mph.")
    if 'n' in change_unit:
        metric_distance = int(int(distance) * 1609.34)
        # metric_speed = int((int(metric_distance)/ 60) / 60)
        kmph = int(metric_distance) / 1000
        print("Well, FYI you'd travel " + str(metric_distance)+ " meters, " + str(kmph) + " kilometers.")
if 'run' in traveling:
    miles_rate = int(distance) // 6
    print("That should take about " + str(miles_rate) + " hours if you run 6mph")
    change_unit = input("Do you want to change the speed?\n:")
    if 'y' in change_unit:
        new_rate = float(input("How many miles per hour will you travel?\n:"))
        time = int(distance) / int(new_rate)
        print("Then your trip would take you " + str(time) + " hours at " + str(new_rate) + "mph.")
    if 'n' in change_unit:
        metric_distance = int(int(distance) * 1609.34)
        # metric_speed = int((int(metric_distance)/ 60) / 60)
        kmph = int(metric_distance) / 1000
        print("Well, FYI you'd travel " + str(metric_distance)+ " meters, " + str(kmph) + " kilometers.")
if 'bik' in traveling:
    miles_rate = int(distance) // (100/15)
    print("That should take about " + str(miles_rate) + " hours if you ride at 15mph.")
    change_unit = input("Do you want to change the speed?\n:")
    if 'y' in change_unit:
        new_rate = float(input("How many miles per hour will you travel?\n:"))
        time = int(distance) / int(new_rate)
        print("Then your trip would take you " + str(time) + " hours at " + str(new_rate) + "mph.")
    if 'n' in change_unit:
        metric_distance = int(int(distance) * 1609.34)
        # metric_speed = int((int(metric_distance)/ 60) / 60)
        kmph = int(metric_distance) / 1000
        print("Well, FYI you'd travel " + str(metric_distance)+ " meters, " + str(kmph) + " kilometers.")
if 'driv' in traveling:
    miles_rate = int(distance) // 60
    print("That should take about " + str(miles_rate) + " hours if you drive 60mph.")
    change_unit = input("Do you want to change the speed?\n:")
    if 'y' in change_unit:
        new_rate = float(input("How many miles per hour will you travel?\n:"))
        time = int(distance) / int(new_rate)
        print("Then your trip would take you " + str(time) + " hours at " + str(new_rate) + "mph.")
    if 'n' in change_unit:
        metric_distance = int(int(distance) * 1609.34)
        # metric_speed = int((int(metric_distance)/ 60) / 60)
        kmph = int(metric_distance) / 1000
        print("Well, FYI you'd travel " + str(metric_distance)+ " meters, " + str(kmph) + " kilometers, \nat " + str(metric_speed) + " meters per second.")
if 'fly' in traveling:
    miles_rate = int(distance) // 400
    print("That should take about " + str(miles_rate) + " hours on a commercial flight(400mph).")
    change_unit = input("Do you want to change the speed?\n:")
    if 'y' in change_unit:
        new_rate = float(input("How many miles per hour will you travel?\n:"))
        time = int(distance) / int(new_rate)
        print("Then your trip would take you " + str(time) + " hours at " + str(new_rate) + "mph.")
    if 'n' in change_unit:
        metric_distance = int(int(distance) * 1609.34)
        metric_speed = int((int(metric_distance)/ 60) / 600)
        kmph = int(metric_distance) / 1000
        print("Well, FYI you'd travel " + str(metric_distance)+ " meters, " + str(kmph) + " kilometers, at " + str(metric_speed) + " meters per second.")

# PORTLAND PUBLIC ART
#
# LAB: PORTLAND PUBLIC ART
#
# Write a module that takes a users location and displays the geographically nearest public art details. Support text search functionality.
#
# Here is the dataset description from the source:
#
# A weekly updated CSV file containing permanently sited works of public art, sourced from the Regional Arts & Culture Council. This searchable database provides information and images of more than 1800 publicly owned artwork in the City and County.
#
# The dataset is availible here but I have also placed it here as public_art.csv
import csv


# latitude = input("Enter Latitude:\n")
# longitude = input("Enter Longitude:\n")
street = input("What street are you on?:\n")
# quadrant = input("Which quadrant are you in?:\n")
def rel_location():
    with open("public_art.csv") as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            if row in street:
                print(row)
            else:
                print("Not nearby.")

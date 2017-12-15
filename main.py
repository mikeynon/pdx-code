
import json
def find_city(city):
    f = open("data.json", 'r')
    data=json.load.(f)

name = (list(f.keys())[0])
latit = data[city]["Position"]["Latitude"]
longit = data[city]["Position"]["Longitude"]

print("{} is located at {} degrees north and {} degrees west.".format(name,latit,longit))

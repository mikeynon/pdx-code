import requests
import math
# r - requests.get('http://api.icnb.com/jokes/random')
# data = r.json()
# joke_id = data["value"]["id"]
# joke = data["value"]["joke"]
# print(joke_id)
# print(joke)
city_select = input("Which city are you looking for?:\n")
payload = {'APPID' : '31245f6b407aa50b66b46a62d86a84e6',"q": city_select}
r = requests.post("http://api.openweathermap.org/data/2.5/weather", params=payload)
data = r.json()
tempf = data["main"]["temp"]*(9/5)-459.67
tempc = data["main"]["temp"]-273.15
roundedf = round(tempf, 2)
roundedc = round(tempc, 2)

temp_select = input("(f)arenheit or (c)elsius?:\n")
if temp_select in "f":
    print("{} Farenheit".format(roundedf))
if temp_select in "c":
    print("{} Celsius".format(roundedc))

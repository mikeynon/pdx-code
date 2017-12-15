import json
f = open("data.json", 'r')
content = f.read()

parsed_json = json.loads(data.json)
print(parsed_json)

# f = open("data.json", 'r')
# content = f.read()
# new_content = content.replace('l', '1')
# f.close()
#
# wf = open("data.json", 'w')
# wf.write(new_content)
# wf.close()


#
# class cities():
#     def __init__(self):
#         self.name = name
#         self.lat = latit
#         self.long = longit
#     def find_name():
#         with open("data.json", 'r') as f:
#         content = f.read()
#     def find_lat(self):
#     def find_long(self):
#
#
#
# print("The Latitude and Longitude of ", find_city() " is ",find_lat()," ", find_long())

# Breakfast: 7AM - 9AM
user_in = input("What time is it?:\n")
if 'am' in user_in.lower():
	meridiem = 'am'
elif 'pm' in user_in.lower():
	meridiem = 'pm'
else:
	meridiem = input("Is that am or pm?:\n")

if meridiem == 'am':
    if int(user_in[0]) in (range(7,9)):
        print("Its Breakfast Time!")
    elif int(user_in[0]) in (range(5,6)):
        print("You shouldn't be eating now!")
    else:
        print("its HAMMER TIME!! CANT TOUCH THIS!")
else:
    if int(user_in[0]) in (range(1,2)):
        print("Its Lunch Time!")
    elif int(user_in[0]) in (range(7,9)):
        print("Its Dinner Time!")
    elif int(user_in[0]) in (range(10,12)):
        print("You shouldn't be eating now!")
    elif int(user_in[0]) in (range(3,6)):
        print("You shouldn't be eating now!")
    else:
        print("its HAMMER TIME!! CANT TOUCH THIS!")

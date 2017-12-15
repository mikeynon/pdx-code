phonebook = {
    1: {'Gump', 'Forest', 9738675309,},
    2: {'Hanks', 'Tom', 2018675309,},
    3: {'Shank', 'Otm', 7328675309,}
        }
initial_action = input("Would you like to [a]dd a new contact, [s]earch or [e}dit an existing contact or (q)uit:\n")
for i in initial_action:
    if initial_action == "a":
        new_contactfn = input("Input new contact: first name:\n")
        new_contactln = input("Input new contact: last name:\n").concat(new_contactfn)
        new_contactpn = input("Input new contact: phone number:\n").concat(new_contactfn)
        # def adding_contact:
        complete_contact = new_contactfs.split()


        print("New Contact Added")

    elif initial_action == "s":
        search_field = input("Search by Last Name:\n")
        filter lambda search_field, phonebook:
            print(phonebook("{} {} \#\: {}").format

        else:
            print(search_field," was not found.")
    # elif initial_action == "e":
    #     contact_update = input("Which contact would you like to edit?:\n")
    #
    #     # search for existing contact
    #     def edit_contact:
    #
    #     # .replace()
    elif initial_action == "q":
        print("Thanks for using the phonebook.")
        exit()

else:
    print("This action is not permitted.")





# 1. create new contact using new_contact index 0 as a list name and as item index 0 in list,
# new_contact index 1 as item 2, and new_contact index 2 as item 3
# 2. add new contact list to phonebook list
# 3. search lists from phonebook and return either formatted list or an else statement

# phone = input("Pleasetype your phone number without spaces or hyphens:\n")
# # insert parenthesis before 0 and 3 index, add space before 3 index, then insert hyphen before 6 index
# charttoinsert = {1: "(", 2: ")", 3: " ", 4: "-"}
#
# def prettynumber(charttoinsert):
#     # for i in phone
#         # (phone[:0], {}, phone[0:2], {}, {}, phone[4:6], {}, phone[6:]).format(charttoinsert(1,2,3,4))
#     return '{}.{}.{}.{}.'.format(phone[:0], {}, phone[0:2], {}, {}, phone[4:6], {}, phone[6:])
# final = phone(prettynumber)
# print(final)
#
# phone = input("Please type your number without spaces or hyphens:\n")
# # insert parenthesis before 0 and 3 index, add space before 3 index, then insert hyphen before 6 index
# charttoinsert = {1: "(", 2: ")", 3: " ", 4: "-"}
# # def prettynumber():
# #     (phone[:0], {1}, phone[0:2], {2}, {3}, phone[4:6], {4}, phone[6:]).format(**charttoinsert)
#
# print("Your number is ",((phone[:0], {1}, phone[0:2], {2}, {3}, phone[4:6], {4}, phone[6:]).format(**charttoinsert)))

# insert parenthesis before 0 and 3 index, add space before 3 index, then insert hyphen before 6 index
# charttoinsert = {1: "(", 2: ")", 3: " ", 4: "-"}
import random
import string



countrydict= {
93:"Afghanistan",
358:"Aland Islands",
355:"Albania",
213:"Algeria",
376:"Andorra",
244:"Angola",
54:"Argentina",
374:"Armenia",
297:"Aruba" ,
247:"Ascension Island",
61:"Australia",
672:"Australian External Territories",
43:"Austria",
994:"Azerbaijan",
973:"Bahrain",
880:"Bangladesh",
375:"Belarus",
32:"Belgium",
501:"Belize",
229:"Benin",
975:"Bhutan",
591:"Bolivia",
599:"Bonaire",
387:"Bosnia and Herzegovina",
267:"Botswana",
55:"Brazil",
246:"British Indian Ocean Territory",
673:"Brunei",
359:"Bulgaria",
226:"Burkina Faso",
257:"Burundi",
855:"Cambodia",
237:"Cameroon",
238:"Cape Verde",
599:"Caribbean Netherlands",
236:"Central African Republic",
235:"Chad",
64:"Chatham Islands",
56:"Chile",
86:"China",
61:"Christmas Island",
57:"Colombia",
269:"Comoros",
242:"Congo, Republic of the",
243:"Congo, Democratic Republic of the",
682:"Cook Islands",
506:"Costa Rica",
225:"Cote d'Ivoire",
385:"Croatia",
53:"Cuba",
599:"Curacao",
357:"Cyprus",
420:"Czech Republic",
45:"Denmark",
253:"Djibouti",
593:"Ecuador",
20:"Egypt",
503:"El Salvador",
240:"Equatorial Guinea",
291:"Eritrea",
372:"Estonia",
251:"Ethiopia",
500:"Falkland Islands",
298:"Faroe Islands",
679:"Fiji",
358:"Finland",
33:"France",
594:"French Guiana",
689:"French Polynesia",
241:"Gabon",
220:"Gambia",
995:"Georgia",
49:"Germany",
233:"Ghana",
350:"Gibraltar",
30:"Greece",
299:"Greenland",
590:"Guadeloupe",
502:"Guatemala",
44:"Guernsey",
224:"Guinea",
245:"Guinea-Bissau",
592:"Guyana",
509:"Haiti",
504:"Honduras",
852:"Hong Kong",
36:"Hungary",
354:"Iceland",
91:"India",
62:"Indonesia",
98:"Iran",
964:"Iraq",
353:"Ireland",
44:"Isle of Man",
972:"Israel",
39:"Italy",
81:"Japan",
44:"Jersey",
962:"Jordan",
254:"Kenya",
686:"Kiribati",
965:"Kuwait",
996:"Kyrgyzstan",
856:"Laos",
371:"Latvia",
961:"Lebanon",
266:"Lesotho",
231:"Liberia",
218:"Libya",
423:"Liechtenstein",
370:"Lithuania",
352:"Luxembourg",
853:"Macau",
389:"Macedonia",
261:"Madagascar",
265:"Malawi",
60:"Malaysia",
960:"Maldives",
223:"Mali",
356:"Malta",
692:"Marshall Islands",
596:"Martinique",
222:"Mauritania",
230:"Mauritius",
262:"Mayotte",
52:"Mexico",
691:"Micronesia",
373:"Moldova",
377:"Monaco",
976:"Mongolia",
382:"Montenegro",
212:"Morocco",
258:"Mozambique",
95:"Myanmar",
264:"Namibia",
674:"Nauru",
977:"Nepal",
31:"Netherlands",
687:"New Caledonia",
64:"New Zealand",
505:"Nicaragua",
227:"Niger",
234:"Nigeria",
683:"Niue",
672:"Norfolk Island",
850:"North Korea",
47:"Norway",
968:"Oman",
92:"Pakistan",
680:"Palau",
970:"Palestine",
507:"Panama",
675:"Papua New Guinea",
595:"Paraguay",
51:"Peru",
63:"Philippines",
64:"Pitcairn Islands",
48:"Poland",
351:"Portugal",
974:"Qatar",
262:"Reunion",
40:"Romania",
7:"Russia",
250:"Rwanda",
599:"Saba",
290:"Saint Helena",
590:"Saint Martin",
508:"Saint Pierre and Miquelon",
685:"Samoa",
378:"San Marino",
239:"Sao Tome and Principe",
966:"Saudi Arabia",
221:"Senegal",
381:"Serbia",
248:"Seychelles",
232:"Sierra Leone",
65:"Singapore",
599:"Sint Eustatius",
421:"Slovakia",
386:"Slovenia",
677:"Solomon Islands",
252:"Somalia",
27:"South Africa",
500:"South Georgia Islands",
82:"South Korea",
211:"South Sudan",
34:"Spain",
94:"Sri Lanka",
249:"Sudan",
597:"Suriname",
47:"Svalbard",
268:"Swaziland",
46:"Sweden",
41:"Switzerland",
963:"Syria",
886:"Taiwan",
992:"Tajikistan",
255:"Tanzania",
66:"Thailand",
670:"Timor-Leste",
228:"Togo",
690:"Tokelau",
676:"Tonga",
290:"Tristan da Cunha",
216:"Tunisia",
90:"Turkey",
993:"Turkmenistan",
688:"Tuvalu",
256:"Uganda",
380:"Ukraine",
971:"United Arab Emirates",
44:"United Kingdom",
1:"United States of America",
598:"Uruguay",
998:"Uzbekistan",
678:"Vanuatu",
379:"Vatican City",
58:"Venezuela",
84:"Vietnam",
808:"Wake Island",
681:"Wallis and Futuna",
967:"Yemen",
260:"Zambia",
263:"Zimbabwe"
}
# def countrycode(first):
#     for i in phone[:-10] or random_num[:-10]

def prettynumber(phone):
    first = phone[:3]
    middle = phone[3:6]
    end = phone[6:]
    print(("Your number is ({}) {}-{} and its registered in/around North America").format(first, middle, end))
    return
def intnumber(phone):
    last = phone[-4:]
    almost = phone[-7:-4]
    second = phone[-10:-7]
    first = phone[:-10]
    print(("Your number is +{}({}) {}-{}.").format(first, second, almost, last))
    print("This number is registered in", countrycode)
    return



def countrycode(countrydict):
    for i in phone[:-10] or random_num[:-10]:
        if i in countrydict:
            print("This number is registed in {}.").format(countrydict)
            return
        else:
            print("Country not found.")

initial = input("Would you like to [l]ook up or [g]enerate a number?:\n").lower()
if initial == "l":
    phone = input("Please type your number without spaces or hyphens:\n")
    if len(phone) == 10:
        prettynumber(phone)
    elif 14 > len(phone) > 10:
        intnumber(phone)
    else:
        print("We're gonna need at least 10 digits.")

elif initial == "g":
    random_num = print(''.join(random.choice(string.digits) for i in (random.randint(10,14))))
    if len(random_num) == 10:
        first = random_num[:3]
        middle = random_num[3:6]
        end = random_num[6:]
        print(("Your number is ({}) {}-{} and its registered in/around North America").format(first, middle, end))
        # return
    elif 14 > len(random_num) > 10:
        last = random_num[-4:]
        almost = random_num[-7:-4]
        second = random_num[-10:-7]
        first = random_num[:-10]
        print(("Your number is +{}({}) {}-{}.").format(first, second, almost, last))
        print("This number is registered in", countrycode)
        # return
else:
    print("Does not compute.")

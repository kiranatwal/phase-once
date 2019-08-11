import random

colorList = ["red", "blue", "yellow", "green"]

card = {
    "color": colorList[random.randint(0,1)],
    "number": random.randint(0,3),
}

deck = {
    "red": 24,
    "blue": 24,
    "green": 24,
    "yellow": 24,
    "zero": 4,
    "one": 8,
    "two": 8,
    "three": 8,
    "four": 8,
    "five": 8,
    "six": 8,
    "seven": 8,
    "eight": 8,
    "nine": 8,
    "ten": 8,
    "eleven" : 8,
    "twelve" : 8,
}



def draw():
    return card["color"] +" "+ str(card["number"])

for x in range(7):
    hand=;
    hand.append(draw());
print hand;
# hand = deal();
# print(hand)

# for cardKind in deck
#     if cardKind == ""


#print(draw())

if card["color"] == "red" and card["number"] ==0:
    deck["red"] = deck["red"]-1,
    deck["zero"] = deck["zero"]-1

elif card["color"] == "red" and card["number"] ==1:
    deck["red"] = deck["red"]-1,
    deck["one"] = deck["one"]-1

elif card["color"] == "red" and card["number"] ==2:
    deck["red"] = deck["red"]-1,
    deck["two"] = deck["two"]-1

elif card["color"] == "red" and card["number"] ==3:
    deck["red"] = deck["red"]-1,
    deck["three"] = deck["three"]-1

elif card["color"] == "red" and card["number"] ==4:
    deck["red"] = deck["red"]-1,
    deck["four"] = deck["four"]-1

# elif card["color"] == "red" and card["number"] ==5:
#     deck["red"] = deck["red"]-1,
#     deck["three"] = deck["three"]-1
#
# elif card["color"] == "red" and card["number"] ==6:
#     deck["red"] = deck["red"]-1,
#     deck[""] = deck[""]-1
#
# elif card["color"] == "red" and card["number"] ==7:
#     deck["red"] = deck["red"]-1,
#     deck[""] = deck[""]-1
#
# elif card["color"] == "red" and card["number"] ==8:
#     deck["red"] = deck["red"]-1,
#     deck[""] = deck[""]-1
#
# elif card["color"] == "red" and card["number"] ==9:
#     deck["red"] = deck["red"]-1,
#     deck[""] = deck[""]-1
#
# elif card["color"] == "red" and card["number"] ==10:
#     deck["red"] = deck["red"]-1,
#     deck[""] = deck[""]-1
#
# elif card["color"] == "red" and card["number"] ==11:
#     deck["red"] = deck["red"]-1,
#     deck[""] = deck[""]-1
#
# elif card["color"] == "red" and card["number"] ==12:
#     deck["red"] = deck["red"]-1,
#     deck[""] = deck[""]-1


# elif card["color"] == "blue":
#     deck["blue"] = deck["blue"]-1
# elif card["color"] == "yellow":
#     deck["yellow"] = deck["yellow"]-1
# elif card["color"] == "green":
#     deck["green"] = deck["green"]-1
# if card["number"] == "0":
#     deck["zero"] == deck["zero"]-1
# elif card["number"] == "1":
#     deck["one"] == deck["one"]-1
# elif card["number"] == "2":
#     deck["two"] == deck["two"]-1
# elif card["number"] == "3":
#     deck["three"] == deck["three"]-1
# elif card["number"] == "4":
#     deck["four"] == deck["four"]-1
# elif card["number"] == "5":
#     deck["five"] == deck["five"]-1
# elif card["number"] == "6":
#     deck["six"] == deck["six"]-1
# elif card["number"] == "7":
#     deck["seven"] == deck["seven"]-1
# elif card["number"] == "8":
#     deck["eight"] == deck["eight"]-1
# elif card["number"] == "9":
#     deck["nine"] == deck["nine"]-1
# elif card["number"] == "10":
#     deck["ten"] == deck["ten"]-1
# elif card["number"] == "11":
#     deck["eleven"] == deck["eleven"]-1
# elif card["number"] == "12":
#     deck["twelve"] == deck["twelve"]-1




# print(deck["blue"],deck["green"],deck["red"],deck["yellow"])
print(deck["zero"],deck["red"])

import numpy as np
import random

global cards
cards = []

for i in range(52):
    cards.append(i)


def color(random_cards):
    cards = []
    for i in range(5):
        cards.append(random_cards[i] // 13)
    return cards

    # 0 = herz
    # 1=karo
    # 2=kreuz
    # 3=pik


def symbols_of_5(random_cards):
    symbols = []
    for i in range(5):
        symbols.append(random_cards[i] % 13)
    return symbols


def five_cards():
    index = 0
    rn = []
    while index < 5:
        randomn = random.randint(0, 51 - index)
        cards[randomn], cards[51 - index] = cards[51 - index], cards[randomn]
        rn.append(cards[51 - index])
        index = index + 1
    return rn


def repetition(random_cards):
    return {item: random_cards.count(item) for item in random_cards}


def paar(random_cards):
    if 2 in repetition(symbols_of_5(random_cards)).values():
        return ("paar")


def drilling(random_cards):
    if 3 in repetition(symbols_of_5(random_cards)).values():
        return ("drilling")


def straße(random_cards):
    sorted_cards = sorted(symbols_of_5(random_cards))
    counter = 0
    for index in range(4):
        if sorted_cards[index] + 1 == sorted_cards[index + 1]:
            counter = counter + 1

    if counter == 4:
        return ("straße")


def flush(random_cards):
    if 5 in repetition(color(random_cards)).values():
        return ("flush")


def full_house(random_cards):
    if 3 in repetition(symbols_of_5(random_cards)).values() and 2 in repetition(symbols_of_5(random_cards)).values():
        return ("full_house")


def vierling(random_cards):
    if 4 in repetition(symbols_of_5(random_cards)).values():
        return ("vierling")


def straight_flush(random_cards):
    sorted_cards = sorted(symbols_of_5(random_cards))
    counter = 0
    for index in range(4):
        if sorted_cards[index] + 1 == sorted_cards[index + 1]:
            counter = counter + 1

    if counter == 4 and 5 in repetition(color(random_cards)).values():
        print("straight_flush")


def check_cards():
    pass

def statistik():
    dict = {"paar", "drilling", "straße", "flush", "full_house", "vierling", "straight_flush"}
    using_cards=five_cards()
    for i in range(100000):
        dict[i] == paar(using_cards)

    return dict

testcards = five_cards()
print("Karten: " + "-" * 50)
print(testcards)
print("Symbole: " + "-" * 49)
print(symbols_of_5(testcards))
print("Anzahl der Symbole: " + "-" * 38)
print(repetition(symbols_of_5(testcards)))
print("Kombinationen: " + "-" * 43)
print(paar(testcards))
print(drilling(testcards))
print(straße(testcards))
print(flush(testcards))
print(full_house(testcards))
print(vierling(testcards))
print(straight_flush(testcards))
print("Statistik: " + "-" * 47)


print(statistik())

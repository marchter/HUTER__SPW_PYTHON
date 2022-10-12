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


def paar(random_cards_symbols):
    if 2 in repetition(random_cards_symbols).values():
        print("paar")


def drilling(random_cards_symbols):
    if 3 in repetition(random_cards_symbols).values():
        print("drilling")



def straße(random_cards_symbols):
    sorted_cards = sorted(random_cards_symbols)
    counter=0
    for index in range(4):
        if sorted_cards[index]+1 == sorted_cards[index + 1]:
            counter=counter+1

    if counter == 4:
        print("strße")

def flush(random_cards):
    if 5 in repetition(color(random_cards)).values():
        print("flush")


def full_house(random_cards_symbols):
    if 3 in repetition(random_cards_symbols).values() and 2 in repetition(random_cards_symbols).values():
        print("full_house")

def vierling(random_cards_symbols):
    if 4 in repetition(random_cards_symbols).values():
        print("vierling")

def straight_flush(random_cards):
    sorted_cards = sorted(symbols_of_5(random_cards))
    counter=0
    for index in range(4):
        if sorted_cards[index]+1 == sorted_cards[index + 1]:
            counter=counter+1

    if counter == 4 and 5 in repetition(color(random_cards)).values():
        print("straight_flush")



testcards = five_cards()
print("Karten: " + "-" * 50)
print(testcards)
print("Symbole: " + "-" * 49)
print(symbols_of_5(testcards))
print("Anzahl der Symbole: " + "-" * 38)
print(repetition(symbols_of_5(testcards)))
print("Kombinationen: " + "-" * 43)
paar(symbols_of_5(testcards))
drilling(symbols_of_5(testcards))
straße(symbols_of_5(testcards))
flush(testcards)
full_house(symbols_of_5(testcards))
vierling(symbols_of_5(testcards))
straight_flush(testcards)
print("Statistik: " + "-" * 47)

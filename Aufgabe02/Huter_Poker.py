import numpy as np
import random

cards = []

for i in range(52):
    cards.append(i)


def color(random_cards):
    cards = []
    for i in range(5):
        cards.append(random_cards[i] // 13)
    return cards

    # 0=herz
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
    return 2 in repetition(symbols_of_5(random_cards)).values()


def drilling(random_cards):
    return 3 in repetition(symbols_of_5(random_cards)).values()


def straße(random_cards):
    sorted_cards = sorted(symbols_of_5(random_cards))
    counter = 0
    for index in range(4):
        if sorted_cards[index] + 1 == sorted_cards[index + 1]:
            counter = counter + 1

    return counter == 4


def flush(random_cards):
    return 5 in repetition(color(random_cards)).values()


def full_house(random_cards):
    return 3 in repetition(symbols_of_5(random_cards)).values() and 2 in repetition(symbols_of_5(random_cards)).values()


def vierling(random_cards):
    return 4 in repetition(symbols_of_5(random_cards)).values()


def straight_flush(random_cards):
    sorted_cards = sorted(symbols_of_5(random_cards))
    counter = 0
    for index in range(4):
        if sorted_cards[index] + 1 == sorted_cards[index + 1]:
            counter = counter + 1

    return counter == 4 and 5 in repetition(color(random_cards)).values()


def highest(using_cards):
    highestnr = 0
    if paar(using_cards):
        highestnr = 1
    elif drilling(using_cards):
        highestnr = 2
    elif straße(using_cards):
        highestnr = 3
    elif flush(using_cards):
        highestnr = 4
    elif full_house(using_cards):
        highestnr = 5
    elif vierling(using_cards):
        highestnr = 6
    elif straight_flush(using_cards):
        highestnr = 7

    return highestnr


def statistik():
    dict = {}
    for i in range(0, 8):
        dict[i] = i
    for i in range(1000000):
        using_cards = five_cards()
        dict[highest(using_cards)] += 1
        # breakpoint()
    return dict


def statistik_prozent(dict):
    print(str(statistik()))
    print("Statistik in %: " + "-" * 47)
    for i in dict.values():
        print(str((i * 100) / 1000000) + "%")


def main():
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
    print("Highest: " + "-" * 50)
    print(highest(testcards))
    print("Statistik: " + "-" * 47)
    print(statistik_prozent(statistik()))


if __name__ == "__main__":
    main()

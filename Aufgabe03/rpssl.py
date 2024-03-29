import random

import pandas as pd
from flask import Flask
import json
import matplotlib.pyplot as plt


symbols = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]


def getInput():
    for i in range(len(symbols)):
        print(str(i) + " equals " + symbols[i])
    user_input = input("Choose between 0 and 4 \n ")
    return int(user_input) if user_input.isdigit() and int(user_input) in range(len(symbols)) else "false input"

def getWinner(p1, p2):
    # überlegen mit wie sie verzweigt sind, also 1 mit die nächsten 2
    # 5 bedeutet dass niemand gewinnt, sonst wird der gewinner zurückgegeben.
    check_value = (p1 - p2) % len(symbols)
    if p1 == p2: return -1
    if check_value == 1 or check_value == 2: return p1
    if check_value == 3 or check_value == 4: return p2


def getWinner2(p1, p2):
    # einfachere methode, einfach schaun ob p2 einer vor oder nach p1 is
    if p1 == p2: return -1
    if p2 == (p1 - 1) % 5 or p2 == (p1 - 2) % 5:
        return p1
    else:
        return p2


def pvp():
    print("The Player that chose " + symbols[getWinner(getInput(), getInput())] + " won!")


def random_pvc():
    # mit print zwar schönere ausgabe aber für datenspeicherung nervig. :D
    # print("The Player that chose "+symbols[getWinner(getInput(),random.randint(0,4))]+" won!" )
    p = getInput()
    c = random.randint(0, len(symbols) - 1)
    pvc_write(p, c)
    return getWinner(p, c)


def ai_pvc():
    file = open("pvc_count.txt", "r")
    dict = {}
    for i in range(0, 5):
        dict[i] = 0

    for i in file.readlines():
        if i.startswith("com won with"):
            dict[int(i[13])] += 1

    most_won = max(dict, key=dict.get)

    p = getInput()
    print("Com chose %s \nThe player that chose %s won" % (most_won, getWinner(p, most_won)))



def impossible_pvc():
    p = getInput()
    c = (p + 1) % 5
    print("Com chose %s \nThe player that chose %s won" % (c, getWinner(p, c)))


def pvc_menu():
    print("What type of player vs com do you want to play?\nWe offer:\n [0] Random\n [1] AI\n [2] impossible")
    methods = [random_pvc, ai_pvc, impossible_pvc]
    inp = input("Choose a option")
    methods[int(inp)]()


def pvc_write(p, c):
    file1 = open("pvc_count.txt", "a")
    if getWinner(p, c) == -1:
        file1.write("\ndraw " + str(p) + str(c))
    elif p == getWinner(p, c):
        file1.write("\np won with " + str(p) + "\ncom lost with " + str(c))
    else:
        file1.write("\ncom won with " + str(c) + "\np lost with " + str(p))
    file1.close()


def pvc_count():
    file1 = open("pvc_count.txt", "r")
    data = str(file1.read())
    return ("\np1 won: " + str(data.count("p won")) + " \ncom won: " + str(data.count("com won")))


def symbols_count():
    file1 = open("pvc_count.txt", "r")
    data = str(file1.read())
    return "\nSymbols used:\n Rock: " + str(data.count("0")) + "\n Paper: " + str(
        data.count("1")) + "\n Scissors: " + str(data.count("2")) + "\n Spock: " + str(
        data.count("3")) + "\n Lizard: " + str(data.count("4"))

def tojson(s):
    file1 = open("pvc_count.txt", "r")
    data = str(file1.read())
    if s == "symbols" or s == str(0):
        return {"rock": (data.count("0")), "paper": (data.count("1")), "scissors": (data.count("2")), "spock": (data.count("3")), "lizard": (data.count("4"))}
    elif s == "wins" or s == str(1):
        return {"p": (data.count("p won")), "c": (data.count("com won")), "draw": (data.count("draw"))}

def statistic():
    return symbols_count() + "\n\n Winners:" + pvc_count()

def plot():
    inp = input("Choose what to plot \n[0]: symbols\n[1]: wins  ")
    dict = (tojson(inp))
    plt.bar(dict.keys(), dict.values())
    plt.show()

def upload():
     app.run()


def menü():
    print("What do you want to play?\nWe offer:\n [0] pvp\n [1] pvc\n [2] statistic\n [3] plot\n [4] upload data")
    #mit liste die methoden beinhalet ohne (), diese werden dann aufgerufen, da nur die Addresse aufgerufen wird
    methods = [pvp, pvc_menu, statistic, plot, upload]
    inp = input("Choose a option")
    methods[int(inp)]()



app = Flask(__name__)

@app.route('/')
def index():
    output = "<a href=/symbols>symbols</a> <br/> <a href=/wins>wins</a>"
    return output

@app.route('/symbols')
def get_symbols():
    #output = statistic().replace('\n', '<br/>')
    output = tojson("symbols")
    return output
@app.route('/wins')
def get_wins():
    #output = statistic().replace('\n', '<br/>')
    output = tojson("wins")
    return output


def main():
    # print(getInput())
    # print(getWinner(0,1))
    # print(getWinner(getInput(), getInput()))
    # pvp()
    # print(pvc())
    # print(pvc_count())
    # pvc_count()
    # print(symbols_count())
    menü()


if __name__ == "__main__":
    main()

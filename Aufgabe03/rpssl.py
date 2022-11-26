import random

symbols = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]


def getInput():
    for i in range(len(symbols)):
        print(str(i) + " equals " + symbols[i])
    user_input = input("Choose between 0 and 4 \n ")
    return int(user_input) if user_input.isdigit() and int(user_input) in range(len(symbols)) else "false input"


def getWinner(p1, p2):
    # überlegen mit wie sie verzweigt sind, also 1 mit die nächsten 2
    # 5 bedeutet dass niemand gewinnt, sonst wird der gewinner zurückgegeben.

    if p1 == p2: return 5
    if (p1 + 1) % 4 == p2: return p2
    if (p1 + 3) % 4 == 2: return p2
    return p1

def pvp():
    print("The Player that chose "+symbols[getWinner(getInput(),getInput())]+" won!" )

def pvc():
    #mit print zwar schönere ausgabe aber für datenspeicherung nervig. :D
    #print("The Player that chose "+symbols[getWinner(getInput(),random.randint(0,4))]+" won!" )
    return getWinner(getInput(),random.randint(0,len(symbols)))


def main():
    # print(getInput())
    #print(getWinner(0,0))
    #print(getWinner(getInput(), getInput()))
    #pvp()
    print(pvc())



if __name__ == "__main__":
    main()

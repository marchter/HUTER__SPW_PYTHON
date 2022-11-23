import random

symbols = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]


def getInput():
    for i in range(len(symbols)):
        print(str(i) + " equals " + symbols[i])
    user_input = input("Choose between 0 and 4 \n ")
    return int(user_input) if user_input.isdigit() and int(user_input) in range(len(symbols )) else "false input"

def getLoser(p1, p2):
    #überlegen mit wie sie verzweigt sind, also 1 mit die nächsten 2
    return p1 if (p1 - (p2 % 5)) in range(0,2) else p2


def main():
    #print(getInput())
    print(getLoser(0,1))

if __name__ == "__main__":
    main()

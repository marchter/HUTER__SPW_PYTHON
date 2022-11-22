import random

symbols = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]


def getInput():
    user_input = input("Choose between 0 and 4 \n ")
    return int(user_input) if user_input.isdigit() else "false input"


def main():
    pass

if __name__ == "__main__":
    main()

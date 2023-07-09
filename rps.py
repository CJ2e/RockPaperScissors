import random
gameEnd = False


def winner(p1, p2):
    if p1 == p2:
        return "Draw"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 wins"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 wins"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 wins"
    else:
        return "Player 2 wins"


def endGame():
    global gameEnd
    if input("Play again? y/n: ").lower().strip() == "n":
        gameEnd = True
    else:
        gameEnd = False


while gameEnd is False:
    options = ["rock", "paper", "scissors"]
    p1 = input("Player 1, choose rock, paper or scissors: ").lower().strip()
    if p1 not in options:
        print("Invalid choice, try again")
        continue
    p2 = random.choice(["rock", "paper", "scissors"])
    print(f"Player 2 chose {p2}")
    print(winner(p1, p2))
    endGame()

# Rock:     A
# Paper:    B
# Scissors: C

# Scoring scheme
# WIN = 6 pts, DRAW = 3pts, LOSS = 0pts
# Rock = 1pts, Paper = 2pts, Scissors = 3pts

# Same as the first problem, but the second column is if you need to win, draw, or lose the round
# Figure out how many points you get based on the guide

# In order to win, choose this
Win = {
    'A': "Paper",
    'B': "Scissors",
    'C': "Rock"
}

# In order to draw, choose this
Draw = {
    'A': "Rock",
    'B': "Paper",
    'C': "Scissors",
}

# In order to lose, choose this
Loss = {
    'A': "Scissors",
    'B': "Rock",
    'C': "Paper"
}

# These are the points for the choice
RPS = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}


def main():
    # Rock:     A X
    # Paper:    B Y
    # Scissors: C Z

    file = open("StrategyGuide.txt", "r")

    lines = file.readlines()

    # Tracker for the score
    score = 0

    for x in lines:
        # LOSE
        if x[2] == "X":
            # Add the points for the thing you choose to make a loss
            score += RPS[Loss[x[0]]]

        # DRAW
        elif x[2] == "Y":
            # Add the points for the thing you choose to make a draw and 3pts for draw
            score += 3 + RPS[Draw[x[0]]]

        # WIN
        elif x[2] == "Z":
            # Add the points for the thing you choose to make a win and 6pts for win
            score += 6 + RPS[Win[x[0]]]

    # Print result
    print(score)
    input("Enter anything to close")


if __name__ == "__main__":
    main()

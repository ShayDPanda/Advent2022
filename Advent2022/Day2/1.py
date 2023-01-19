# Rock:     A X
# Paper:    B Y
# Scissors: C Z

# Do rock paper scissors, but calculate a score based on a guide;
# The first column is your opponent and the second column is you BUT its also encoded;

# You get points for result as well as what you selected to throw out
# WIN = 6 pts, DRAW = 3pts, LOSS = 0pts
# Rock = 1pts, Paper = 2pts, Scissors = 3pts

# Figure out how many points you get based on the guide

# In order to win, this is the pair
Win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

# In order to draw, this is the pair
Draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

# These are the points for what you threw out
RPS = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


def main():
    file = open("StrategyGuide.txt", "r")

    lines = file.readlines()

    # The tracker for the score
    score = 0

    for x in lines:
        # Check for winning pair
        if x[2] == Win[x[0]]:
            # Add points for win
            score += 6

        # Check for draw pair
        elif x[2] == Draw[x[0]]:
            # Add points for loss
            score += 3
        # Assume all else is a loss

        # Add score for whatever was used
        score += RPS[x[2]]

    # Print result
    print(score)
    input("Enter anything to close")


if __name__ == "__main__":
    main()

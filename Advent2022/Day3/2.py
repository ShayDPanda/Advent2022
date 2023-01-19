# Each string is a set of compartments.
# The first half is one rucksack while the second is a different rucksack
# Each pair has one similar character between them

# Find that similar character and add its value to the total and repeat for each compartment


# Get the number's value
def getNum(alpha):
    # Convert from ascii to decimal then modify for the problem's values
    # lowercase = 1-26; uppercase = 27-52
    if alpha.islower():
        return ord(alpha) - 96
    else:
        return ord(alpha) - 38


# Find the similar character then return the number assigned
def findSimilar(firstSack, secondSack):
    # Go through the list in the first sack...
    for x in list(firstSack):

        # If a pair is found...
        if x in secondSack:
            # Return the value of the character
            return getNum(x)

    # There shouldn't be one that doesn't have a pair, but just in case
    print("Error occurred:" + firstSack + " " + secondSack)
    return 0


def main():
    file = open("ruckSack.txt", 'r')
    lines = file.readlines()

    # Record the total priority
    priority = 0

    # For each set of compartments...
    for x in lines:

        # Strip the newline
        x = x.strip()
        # Find where half is
        half = int(len(x) / 2)

        # Add the result
        priority += findSimilar(x[0:half], x[half: len(x)])

    # Print the result
    print(priority)


if __name__ == "__main__":
    main()

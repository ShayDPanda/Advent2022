# Same as the first, but this time its each set of three lines is one group (3 rucksacks)

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
def findSimilar(firstSack, secondSack, thirdSack):
    # Go through the list in the first sack...
    for x in list(firstSack):

        # If it exists in both the second and third stack...
        if x in secondSack and x in thirdSack:
            # Return the character's value
            return getNum(x)

    # There shouldn't be one that doesn't have a match, but just in case
    print("Error occurred:" + firstSack + " " + secondSack + " " + thirdSack)
    return 0


def main():
    file = open("ruckSack.txt", 'r')
    lines = file.readlines()

    # Record the total priority
    priority = 0

    # Current number of bags recorded
    current = 1
    # Setup
    rucksackOne = ""
    rucksackTwo = ""

    # For each set of compartments...
    for x in lines:

        # first bag
        if current == 1:
            rucksackOne = x.strip()

        # second bag
        elif current == 2:
            rucksackTwo = x.strip()

        # third bag
        else:
            rucksackThree = x.strip()

            # Add the result
            priority += findSimilar(rucksackOne, rucksackTwo, rucksackThree)
            # Reset current
            current = 0

        # Move on to the next bag
        current += 1

    # Print the result
    print(priority)


if __name__ == "__main__":
    main()

# Number of columns for crates
numCol = 9


def main():
    file = open("cargo.txt", 'r')
    line = file.readline()

    # Get how many layers of crates there are
    initCrateTall = 0
    while "1" not in line:
        initCrateTall += 1
        line = file.readline()

    file.seek(0)

    # Create the 2d arrays
    # One to read in the crates
    crateFile = [["" for x in range(initCrateTall)] for y in range(numCol)]
    # One for the actual order of the crates
    crateArray = []
    for x in range(numCol):
        crateArray.append([])

    # Read in the crates
    for y in range(initCrateTall):
        for x in range(numCol):
            crate = list(file.read(4))

            # If there is a crate present, record it
            if crate[1] != ' ':
                crateFile[x][y] = crate[1]

    # Reverse the order correctly so the bottom crates are first
    counter = 0
    for x in crateFile:
        for y in reversed(x):
            if y != "":
                crateArray[counter].append(y)
        counter += 1

    # Skip the crate numbering
    line = file.readline()
    # Skip the newline
    line = file.readline()
    # Read the rest of the file
    line = file.readlines()

    for command in line:
        command = command.split()
        numCrates = int(command[1])
        colFrom = int(command[3])
        colTo = int(command[5])

        for i in reversed(range(1, numCrates + 1)):
            crateArray[colTo - 1].append(crateArray[colFrom - 1][-i])

        for i in range(numCrates):
            crateArray[colFrom - 1].pop(-1)

    for column in crateArray:
        print(column[-1], end="")


if __name__ == "__main__":
    main()

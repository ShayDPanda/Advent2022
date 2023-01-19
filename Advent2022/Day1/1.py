# There is a list of elves with bags of food.
# Find the elf with the most food and what that calorie count is
def main():
    file = open('elfCal.txt', 'r')

    line = file.readlines()
    # Current Largest Calorie count
    cal = 0

    # Current calorie count of the elf
    currentCal = 0

    for x in line:
        # If that elf's list ended...
        if x is "\n":
            # Check if that elf had a higher calorie count than the current largest
            if currentCal > cal:
                cal = currentCal

            # Reset the count for the next elf
            currentCal = 0

        # Keep adding to current elf, strip new line
        else:
            currentCal += int(x.strip())

    # Print result
    print(cal)
    input("Enter anything to close")


if __name__ == "__main__":
    main()

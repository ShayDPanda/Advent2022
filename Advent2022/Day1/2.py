# Same as part one, but this time add up the three largest calories
def main():
    file = open('elfCal.txt', 'r')

    line = file.readlines()

    # Calories of the three largest
    firstCal = 0
    secondCal = 0
    thirdCal = 0

    # Current count of the current elf
    currentCal = 0

    for x in line:

        # If the elf's list is over...
        if x is "\n":
            # Check if the calorie total is bigger than anything in the list
            if currentCal > firstCal:
                thirdCal = secondCal
                secondCal = firstCal
                firstCal = currentCal

            elif currentCal > secondCal:
                thirdCal = secondCal
                secondCal = currentCal

            elif currentCal > thirdCal:
                thirdCal = currentCal

            # Reset the calorie count
            currentCal = 0

        # Otherwise keep adding to the current elf, strip the new line
        else:
            currentCal += int(x.strip())

    # Print the result
    print(firstCal + secondCal + thirdCal)
    input("Enter anything to close")


if __name__ == "__main__":
    main()

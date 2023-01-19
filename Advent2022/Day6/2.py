def checkDuplicate(charList):
    if charList[0] == charList[1] or charList[0] == charList[2] or charList[0] == charList[3]:
        return True

    if charList[1] == charList[2] or charList[1] == charList[3]:
        return True

    if charList[2] == charList[3]:
        return True

    return False


def main():
    file = open("datastream.txt", 'r')
    line = list(file.readline())
    line.pop(-1)

    charArray = []

    for i in range(3):
        charArray.append(line[0])
        line.pop(0)

    i = 2
    for currentChar in line:
        i += 1
        charArray.append(currentChar)
        if checkDuplicate(charArray):
            charArray.pop(0)
        else:
            break

    print("\nAnswer:", i + 1, charArray)


if __name__ == "__main__":
    main()

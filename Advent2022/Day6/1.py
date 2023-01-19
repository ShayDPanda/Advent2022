def checkDuplicate(charList):
    for i in range(len(charList)):
        obj = charList[i]
        charList.remove(charList[i])
        if obj in charList:
            charList.insert(i, obj)
            return True
        else:
            charList.insert(i, obj)

    return False


def main():
    file = open("datastream.txt", 'r')
    line = list(file.readline())
    line.pop(-1)

    charArray = []

    for i in range(13):
        charArray.append(line[0])
        line.pop(0)

    i = 12
    for currentChar in line:
        i += 1
        charArray.append(currentChar)
        if checkDuplicate(charArray):
            charArray.pop(0)
        else:
            break

    print("\nAnswer:", i + 1)


if __name__ == "__main__":
    main()

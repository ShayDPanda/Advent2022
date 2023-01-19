def main():
    file = open("Pairs.txt", 'r')
    lines = file.readlines()

    count = 0
    for x in lines:
        x = x.strip()
        x = x.split(",")

        left = x[0].split("-")
        right = x[1].split("-")

        if int(left[0]) <= int(right[0]) <= int(left[1]) \
                or int(left[0]) <= int(right[1]) <= int(left[1])\
                or int(right[0]) <= int(left[0]) <= int(right[1])\
                or int(right[0]) <= int(left[1]) <= int(right[1]):
            count += 1

    print(count)


if __name__ == "__main__":
    main()

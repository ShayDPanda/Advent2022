def main():
    file = open("directory.txt", 'r')

    while True:
        line = file.readline().strip()
        print(line)
        if not line:
            break


if __name__ == "__main__":
    main()

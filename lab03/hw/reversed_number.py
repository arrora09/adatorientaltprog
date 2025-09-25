

def reversedNumber(num):
    return int(str(num)[::-1])


def main():
    print(1234, reversedNumber(1234))
    print(4321, reversedNumber(4321))
    print(145, reversedNumber(145))


if __name__ == "__main__":
    main()


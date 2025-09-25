import sys


def main():
    try:
        print(int(sys.argv[1]) + int(sys.argv[2]))
    except IndexError:
        print("Nincs megadva két szám")


if __name__ == "__main__":
    main()
def cleaner(s):
    return "".join(s.split())


def main():
    print("192.20.246.138:\n 6666")
    print(cleaner("192.20.246.138:\n 6666"))

    print("206.130.99.82:\n8080")
    print(cleaner("206.130.99.82:\n8080"))


if __name__ == "__main__":
    main()

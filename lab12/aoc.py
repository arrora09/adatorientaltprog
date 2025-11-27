inp = """(())"""


def main():
    pos = 0
    for d in inp:
        if d == "(":
            pos += 1
        elif d == ")":
            pos -= 1

    print(pos)


if __name__ == "__main__":
    main()

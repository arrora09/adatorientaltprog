#!/usr/bin/env python3


def main():
    coords = set()
    x = 0
    y = 0
    coords.add((x, y))
    with open("input.txt", "r") as f:
        for l in f:
            line = l.strip()
            for direction in line:
                if direction == ">":
                    x += 1
                elif direction == "<":
                    x -= 1
                elif direction == "^":
                    y += 1
                elif direction == "v":
                    y -= 1
                coords.add((x, y))

        print(len(coords))


if __name__ == "__main__":
    main()

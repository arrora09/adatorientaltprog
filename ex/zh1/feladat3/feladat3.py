#!/usr/bin/env python3


def generate_pascal(h):
    pascal = [[1]]

    for i in range(h - 1):
        nums = []
        for j in range(len(pascal[i]) + 1):
            if j == 0 or j == len(pascal[i]):
                nums.append(1)
            else:
                nums.append(pascal[i][j - 1] + pascal[i][j])
        pascal.append(nums)

    return pascal


def main():
    pascal = generate_pascal(20)
    while True:
        inp = input("A sor indexe (kilépés: 0): ")
        if int(inp) == 0:
            break
        out = pascal[int(inp) - 1]
        print(" ".join([str(n) for n in out]))

    print("bye")


if __name__ == "__main__":
    main()

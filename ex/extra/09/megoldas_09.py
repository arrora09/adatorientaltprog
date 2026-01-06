#!/usr/bin/env python3


def main():
    with open("list1.txt", "r", encoding="utf-8") as f:
        list1 = set(line.strip() for line in f)

    with open("list2.txt", "r", encoding="utf-8") as f:
        list2 = set(line.strip() for line in f)

    common = list1 & list2
    unique = (list1 | list2) - common

    # Statisztika
    print(f"List1 elemek: {len(list1)}")
    print(f"List2 elemek: {len(list2)}")
    print(f"Közös elemek: {len(common)}")
    print(f"Egyedi elemek: {len(unique)}")

    with open("common.txt", "w", encoding="utf-8") as outF:
        for item in sorted(common):
            outF.write(item + "\n")
    print("-- common.txt was created")

    with open("unique.txt", "w", encoding="utf-8") as outF:
        for item in sorted(unique):
            outF.write(item + "\n")
    print("-- unique.txt was created")


if __name__ == "__main__":
    main()

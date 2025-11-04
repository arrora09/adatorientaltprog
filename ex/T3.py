import sys


def karakter_szamlalo(text):
    d = {}

    for c in text:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def task3():
    if len(sys.argv) > 2:
        print("Hiba! A program csak egyetlen egy parancssori argumentumot fogad el!")
        return
    elif len(sys.argv) < 2:
        print("Hiba! A programnak kötelező megadni egy parancssori argumentumot!")
        return

    eredmeny = karakter_szamlalo(sys.argv[1])
    for e in eredmeny:
        print(f"{e} - {eredmeny[e]}")


if __name__ == "__main__":
    task3()

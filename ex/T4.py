#!/usr/bin/env python3
import sys


def task4():
    if len(sys.argv) != 2:
        print("Hiba! Meg kell adni egy(!) darab parancssori argumentumot a működéshez!")
        return

    arg = sys.argv[1]

    if len(arg) < 10:
        print("Hiba! A megadott parancssori argumentum túl rövid!")
        return
    elif len(arg) > 10:
        print("Hiba! A megadott parancssori argumentum túl hosszú!")
        return

    l = [ord(c) for c in arg]

    paros = []
    paratlan = []

    for n in l:
        if n % 2 == 0:
            paros.append(int(n * 1.5))
        else:
            paratlan.append(-2 * n)

    print(paros + paratlan)


if __name__ == "__main__":
    task4()

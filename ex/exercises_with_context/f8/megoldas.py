import json
import random
import sys


def generalCim(adatok):
    prefix = random.choice(adatok["prefixek"])
    fonev = random.choice(adatok["fonevek"])
    ige = random.choice(adatok["igek"])
    kovetkezmeny = random.choice(adatok["kovetkezmenyek"])

    return f"{prefix} {fonev} {ige} {kovetkezmeny} | Python Tutorial"


def tesztGeneralas(adatok, n):
    cimek = set()

    max_probalkozsok = n * 100
    probalkozsok = 0

    while len(cimek) < n and probalkozsok < max_probalkozsok:
        cim = generalCim(adatok)
        cimek.add(cim)
        probalkozsok += 1

    return list(cimek)


def main():
    try:
        with open("cimek_adatok.json", "r", encoding="utf-8") as f:
            adatok = json.load(f)

        n = 5
        if len(sys.argv) > 1:
            try:
                n = int(sys.argv[1])
            except ValueError:
                print("Hiba! Érvénytelen szám!")
                return

        cimek = tesztGeneralas(adatok, n)

        print(f"Generált címek ({len(cimek)} db):")
        print()

        for i, cim in enumerate(cimek, 1):
            print(f"{i}. {cim}")

    except FileNotFoundError:
        print("Hiba! A cimek_adatok.json fájl nem található!")
    except Exception as e:
        print(f"Hiba! {e}")


if __name__ == "__main__":
    main()

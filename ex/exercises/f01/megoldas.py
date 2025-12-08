import json
import sys
import numpy
import numpy as np


def main() -> None:
    if len(sys.argv) != 2:
        print("Hiba! Nem megfelelő argumentum szám!")
        return

    keresett = sys.argv[1]

    with open("eredmenyek.json") as f:
        li = json.loads(f.read())

        talalt = False

        for obj in li["eredmenyek"]:
            if obj["kod"] == keresett:
                kod = obj["kod"]
                np_pontok = np.array(obj["pontok"])

                osszpont = np.sum(np_pontok)
                atlag = np.mean(np_pontok)
                med = np.median(np_pontok)
                minPont = np.min(np_pontok)
                maxPont = np.max(np_pontok)
                szoras = np.std(np_pontok)

                legjobbFeladat = obj["pontok"].index(maxPont) + 1

                print(f"Kód: {kod}")
                print(f"Összpontszám: {osszpont}")
                print(f"Átlag: {atlag}")
                print(f"Medián: {med}")
                print(f"Minimum pontszám: {minPont}")
                print(f"Maximum pontszám: {maxPont}")
                print(f"Szórás: {szoras:.2f}")
                print(f"Legjobban sikerült feladat sorszáma: {legjobbFeladat}")
                print(f'Teljesítette? {"Igen" if osszpont >= 21 else "Nem"}')

                talalt = True

        if not talalt:
            print("Hiba! Nincs ilyen kódú megoldás!")


if __name__ == "__main__":
    main()

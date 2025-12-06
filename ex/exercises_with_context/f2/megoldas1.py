import json
from typing import List, Dict, Union
import math


def betolt_gyakorlatok(
    fajlnev="gyakorlatok.json",
):
    try:
        with open(fajlnev, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Hiba! A {fajlnev} fájl nem található!")
        exit(1)


def kereses_nev_alapjan(gyakorlatok, nev):
    talalatok = [gy for gy in gyakorlatok if gy["név"] == nev]
    return talalatok[0] if talalatok else None


def main():
    """Fő függvény."""
    gyakorlatok = betolt_gyakorlatok()

    # Gyakorlat nevének bekérése
    nev: str = input("Adja meg a gyakorlat nevét: ").strip()

    if not nev:
        print("Hiba! Nem adott meg gyakorlat nevet!")
        return

    gyakorlat = kereses_nev_alapjan(gyakorlatok, nev)

    if gyakorlat is None:
        print("Hiba! Nincs ilyen nevű gyakorlat!")
        return

    ossz_kaloria_sorozat = gyakorlat["ismetles"] * gyakorlat["kaloriaszam"]
    szukseges_sorozatok = math.ceil(450 / ossz_kaloria_sorozat)

    print(f"Összes elégetett kalória egy sorozatban: {ossz_kaloria_sorozat} kcal")
    print(f"A pogácsa elégetéséhez szükséges sorozatok száma: {szukseges_sorozatok}")


if __name__ == "__main__":
    main()

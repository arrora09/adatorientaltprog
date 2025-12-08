def idopont_masodpercbe(idopont_str):
    reszek = idopont_str.split(":")

    if len(reszek) == 2:
        return int(reszek[0]) * 60 + int(reszek[1])
    else:
        return 0


def masodperc_idopontta(masodperc):
    ora = masodperc // 3600
    perc = (masodperc % 3600) // 60
    mp = masodperc % 60

    if ora > 0:
        return f"{ora:02d}:{perc:02d}:{mp:02d}"
    else:
        return f"{perc:02d}:{mp:02d}"


def feldolgoz_sort(sor):
    sor = sor.strip()
    if not sor:
        return None

    if " - " in sor:
        reszek = sor.split(" - ", 1)
        idopont = reszek[0]
        szoveg = reszek[1]
        return (idopont, szoveg)

    if " Idő: " in sor:
        reszek = sor.split(" Idő: ", 1)
        idopont = reszek[0]
        szoveg = reszek[1]
        return (idopont, szoveg)

    if sor.startswith("[") and "]" in sor:
        zaro_index = sor.index("]")
        idopont = sor[1:zaro_index]
        szoveg = sor[zaro_index + 1 :].strip()
        return (idopont, szoveg)

    return None


def main():
    feliratok = []
    fajlok = [
        "feliratok/felirat1.txt",
        "feliratok/felirat2.txt",
        "feliratok/felirat3.txt",
    ]
    sikeres_fajlok = 0

    for fajl in fajlok:
        try:
            with open(fajl, "r", encoding="utf-8") as f:
                for sor in f:
                    eredmeny = feldolgoz_sort(sor)
                    if eredmeny:
                        idopont, szoveg = eredmeny
                        masodperc = idopont_masodpercbe(idopont)
                        feliratok.append((masodperc, szoveg))

            sikeres_fajlok += 1

        except FileNotFoundError:
            print(f"Figyelmeztetés: {fajl} nem található!")

    if sikeres_fajlok == 0:
        print("Hiba! Egyetlen felirat fájl sem olvasható be!")
        return

    feliratok_rendezve = sorted(feliratok, key=lambda x: x[0])

    max_masodperc = feliratok_rendezve[-1][0]
    max_perc = max_masodperc // 60
    max_mp = max_masodperc % 60

    print(f"Beolvasott feliratok: {sikeres_fajlok} fájl")
    print(f"Összes feliratsor: {len(feliratok_rendezve)}")
    print()
    print("Egyesített feliratok időrendben:")

    for masodperc, szoveg in feliratok_rendezve:
        idopont_str = masodperc_idopontta(masodperc)
        print(f"[{idopont_str}] {szoveg}")

    print()
    print(f"Teljes videóhossz: {max_perc} perc {max_mp} másodperc ({max_masodperc} mp)")


if __name__ == "__main__":
    main()

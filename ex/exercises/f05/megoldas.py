def main():
    try:
        with open("jelszogeneralas.txt", "r", encoding="utf-8") as f:
            tartalom = f.read()

        kedvenc_szam = None
        keresztnev = None
        titkos_kod = None

        for sor in tartalom.split("\n"):
            if "Kedvenc szám:" in sor:
                kedvenc_szam = sor.split(":")[1].strip()
            elif "Keresztnév:" in sor:
                keresztnev = sor.split(":")[1].strip()
            elif "Titkos kód:" in sor:
                titkos_kod = sor.split(":")[1].strip()

        kedvenc_feldolgozott = "".join(
            [kedvenc_szam[i] for i in range(1, len(kedvenc_szam), 2)]
        )

        keresztnev_feldolgozott = keresztnev[::-1].upper()

        titkos_kod_feldolgozott = "".join(
            [titkos_kod[i] for i in range(0, len(titkos_kod), 2)]
        )

        jelszo = f"{kedvenc_feldolgozott}_{keresztnev_feldolgozott}_{titkos_kod_feldolgozott}"

        print("=== Jelszó Visszafejtés ===")
        print()
        print(f"Kedvenc szám feldolgozva: {kedvenc_feldolgozott}")
        print(f"Keresztnév feldolgozva: {keresztnev_feldolgozott}")
        print(f"Titkos kód feldolgozva: {titkos_kod_feldolgozott}")
        print()
        print(f"Visszafejtett jelszó: {jelszo}")
        print()
        print("Próbálja ki ezt a jelszót a laborrendszerbe való belépéshez!")

    except FileNotFoundError:
        print("Hiba! A jelszogeneralas.txt fájl nem található!")
    except Exception as e:
        print(f"Hiba! {e}")


if __name__ == "__main__":
    main()

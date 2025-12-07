import json
import numpy as np


def main():
    try:
        with open("wow_raidek.json", "r", encoding="utf-8") as f:
            raidek = json.load(f)

        raid_idok = np.array([raid["hossz_perc"] for raid in raidek])
        dps_ertekek = np.array([raid["dps"] for raid in raidek])

        atlag_ido = np.mean(raid_idok)
        median_ido = np.median(raid_idok)
        szoras_ido = np.std(raid_idok)
        teljes_ido_perc = np.sum(raid_idok)
        teljes_ido_ora = teljes_ido_perc / 60

        min_ido_idx = np.argmin(raid_idok)
        max_ido_idx = np.argmax(raid_idok)

        atlag_dps = np.mean(dps_ertekek)
        median_dps = np.median(dps_ertekek)
        min_dps = np.min(dps_ertekek)
        max_dps = np.max(dps_ertekek)

        sikeres = [r for r in raidek if r["boss_killed"]]
        sikertelen = [r for r in raidek if not r["boss_killed"]]

        marathon_raidek = [r for r in raidek if r["hossz_perc"] >= 180]

        high_dps_raidek = [r for r in raidek if r["dps"] > 50000]

        print("Statisztikák:")
        print()
        print(f"Összes raid: {len(raidek)}")
        print()
        print(" RAID IDŐ STATISZTIKÁK:")
        print(f"- Átlagos raid idő: {atlag_ido:.2f} perc ({atlag_ido/60:.2f} óra)")
        print(f"- Medián raid idő: {median_ido:.2f} perc")
        print(f"- Szórás: {szoras_ido:.2f} perc")
        print(f"- Teljes raid idő: {teljes_ido_ora:.2f} óra ({teljes_ido_perc} perc)")
        print()
        print(
            f"Legrövidebb raid: {raid_idok[min_ido_idx]} perc ({raidek[min_ido_idx]['raid_nev']})"
        )
        print(
            f"Leghosszabb raid: {raid_idok[max_ido_idx]} perc ({raidek[max_ido_idx]['raid_nev']})"
        )
        print()
        print("DPS STATISZTIKÁK:")
        print(f"- Átlagos DPS: {atlag_dps:,.2f}")
        print(f"- Medián DPS: {median_dps:,.2f}")
        print(f"- Minimum DPS: {min_dps:,} (Legrosszabb nap... Senki sem pullolt jól)")
        print(f"- Maximum DPS: {max_dps:,} (LEGEND! Mindenki büszke volt!)")
        print()
        print("TELJESÍTMÉNY:")
        print(
            f"- Sikeres boss kill-ek: {len(sikeres)} ({len(sikeres)/len(raidek)*100:.2f}%)"
        )
        print(f"- Wipe-ok: {len(sikertelen)} ({len(sikertelen)/len(raidek)*100:.2f}%)")
        print(f"- Win rate: {len(sikeres)/len(raidek)*100:.2f}%")
        print()
        print(f' "Marathon" raidek (180+ perc): {len(marathon_raidek)}')
        print()
        print("High DPS raidek (50,000+ DPS):")
        for raid in high_dps_raidek:
            print(f"- {raid['boss_nev']} ({raid['raid_nev']}) - {raid['dps']:,} DPS")
        print()
        print(f"FIGYELMEZTETÉS: {teljes_ido_ora:.2f} óra raidelt az elmúlt héten.")

    except FileNotFoundError:
        print("Hiba! A wow_raidek.json fájl nem található!")
    except Exception as e:
        print(f"Hiba! {e}")


if __name__ == "__main__":
    main()

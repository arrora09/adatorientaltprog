import json
import sys


def main():
    if len(sys.argv) != 2:
        print("Hiba! Nem adott meg napszámot paraméterként!")
        return

    try:
        x_nap = int(sys.argv[1])
    except ValueError:
        print("Hiba! Érvénytelen napszám!")
        return

    try:
        with open("emailek.json", "r", encoding="utf-8") as f:
            emails = json.load(f)

        valaszra_varo = [
            email
            for email in emails
            if not email["valaszolt"] and email["kuldott"] > x_nap
        ]

        valaszra_varo_rendezve = sorted(
            valaszra_varo, key=lambda x: x["kuldott"], reverse=True
        )

        osszes_email = len(emails)
        valaszoltak = [email for email in emails if email["valaszolt"]]
        nem_valaszoltak = [email for email in emails if not email["valaszolt"]]

        valaszolt_szam = len(valaszoltak)
        nem_valaszolt_szam = len(nem_valaszoltak)

        print("=== Email Follow-up Manager ===")
        print()
        print(f"Keresés: {x_nap} napnál régebbi, nem válaszolt emailek")
        print()
        print(f"VÁLASZRA VÁRÓ EMAILEK (régebbi mint {x_nap} nap):")
        print()

        if valaszra_varo_rendezve:
            for i, email in enumerate(valaszra_varo_rendezve, 1):
                print(f"{i}. {email['nev']} ({email['email']})")
                print(f"   Tárgy: {email['targy']}")
                print(f"   Küldve: {email['kuldott']} napja")
                print()
        else:
            print("Nincs ilyen email!")
            print()

        print("STATISZTIKA:")
        print(f"- Összes email: {osszes_email}")
        print(
            f"- Már válaszoltak: {valaszolt_szam} ({valaszolt_szam/osszes_email*100:.2f}%)"
        )
        print(
            f"- Még nem válaszoltak: {nem_valaszolt_szam} ({nem_valaszolt_szam/osszes_email*100:.2f}%)"
        )

        if nem_valaszolt_szam > 0:
            arany = len(valaszra_varo_rendezve) / nem_valaszolt_szam * 100
            print(
                f"- Ebből {x_nap}+ napos: {len(valaszra_varo_rendezve)} ({arany:.2f}%)"
            )

        if nem_valaszoltak:
            legregebbi = max(nem_valaszoltak, key=lambda x: x["kuldott"])
            print()
            print(
                f"Legrégebbi válaszolatlan email: {legregebbi['kuldott']} napja ({legregebbi['nev']})"
            )

        if valaszra_varo_rendezve:
            print()
            print("💡 Javaslat: Ideje küldeni egy follow-up emailt!")

    except FileNotFoundError:
        print("Hiba! Az emails.json fájl nem található!")
    except json.JSONDecodeError:
        print("Hiba! Hibás JSON formátum!")
    except Exception as e:
        print(f"Hiba! {e}")


if __name__ == "__main__":
    main()

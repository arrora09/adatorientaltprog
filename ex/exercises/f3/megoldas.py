import json


class BankSzamla:
    def __init__(self, bank_nev, egyenleg, havi_limit, eddig_koltott):
        self.bank_nev = bank_nev
        self.egyenleg = egyenleg
        self.havi_limit = havi_limit
        self.eddig_koltott = eddig_koltott

    def __str__(self):
        return f"{self.bank_nev} - {self.egyenleg} Ft (limit: {self.eddig_koltott}/{self.havi_limit} Ft)"

    def koltes(self, osszeg):
        if self.eddig_koltott + osszeg > self.havi_limit:
            raise ValueError(
                f"A költés túllépi a havi limitet! ({self.eddig_koltott}/{self.havi_limit} Ft felhasználva)"
            )

        self.egyenleg -= osszeg
        self.eddig_koltott += osszeg

    def meg_kolthetek(self, osszeg):
        return self.eddig_koltott + osszeg <= self.havi_limit

    def __lt__(self, other):
        return self.egyenleg < other.egyenleg


def main():
    try:
        with open("bankok.json", "r", encoding="utf-8") as f:
            bankok_data = json.load(f)

        bankok = []
        for bank_data in bankok_data:
            bank = BankSzamla(
                bank_data["bank_nev"],
                bank_data["egyenleg"],
                bank_data["havi_limit"],
                bank_data["eddig_koltott"],
            )
            bankok.append(bank)

        bank_nev = input("Adja meg a bank nevét: ").strip()

        if not bank_nev:
            print("Hiba! Nem adott meg bank nevet!")
            return

        bank = None
        for b in bankok:
            if b.bank_nev == bank_nev:
                bank = b
                break

        if bank is None:
            print("Hiba! Nincs ilyen bank a rendszerben!")
            return

        try:
            osszeg_input = input("Adja meg a költeni kívánt összeget (Ft): ").strip()
            osszeg = int(osszeg_input)
        except ValueError:
            print("Hiba! Érvénytelen összeg!")
            return

        try:
            bank.koltes(osszeg)
            print(f"Sikeres költés! Új egyenleg: {bank.egyenleg} Ft")
            print(
                f"Havi limitből felhasználva: {bank.eddig_koltott} / {bank.havi_limit} Ft"
            )
        except ValueError as e:
            print(f"Hiba! {e}")

        print()
        print("Bankszámlák egyenleg szerint:")
        bankok_rendezve = sorted(bankok)
        for i, b in enumerate(bankok_rendezve, 1):
            print(f"{i}. {b}")

    except FileNotFoundError:
        print("Hiba! A bankok.json fájl nem található!")
    except Exception as e:
        print(f"Hiba! {e}")


if __name__ == "__main__":
    main()

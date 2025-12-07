import json
import math


def osszes_kaloria_sorozat(gyakorlat):
    return gyakorlat["ismetles"] * gyakorlat["kaloriaszam"]


def leghatekonyabb_gyakorlat(gyakorlatok, cel_kaloria):
    eredmenyek = [
        {
            "gyakorlat": gy,
            "sorozatok": math.ceil(cel_kaloria / osszes_kaloria_sorozat(gy)),
            "ossz_ismetles": math.ceil(cel_kaloria / osszes_kaloria_sorozat(gy))
            * gy["ismetles"],
        }
        for gy in gyakorlatok
    ]

    legjobb = min(eredmenyek, key=lambda x: x["ossz_ismetles"])

    return legjobb


def main():
    fajlnev = "gyakorlatok.json"

    try:
        with open(fajlnev, "r", encoding="utf-8") as f:
            gyakorlatok = json.load(f)
    except FileNotFoundError:
        print(f"Hiba! A {fajlnev} fájl nem található!")
        return
    except json.JSONDecodeError:
        print(f"Hiba! A {fajlnev} fájl hibás JSON formátumú!")
        return

    #####################################################

    rendezett = sorted(
        gyakorlatok, key=lambda gy: osszes_kaloria_sorozat(gy), reverse=True
    )

    print("Összes gyakorlat kalóriaégetés szerint:")
    for i, gy in enumerate(rendezett, 1):
        ossz_kal = osszes_kaloria_sorozat(gy)
        print(f"{i}. {gy['név']} - {ossz_kal} kcal")
    print()

    #####################################################

    print("Leghatékonyabb gyakorlat 450 kcal eléréséhez:")
    legjobb = leghatekonyabb_gyakorlat(gyakorlatok, 450)
    gy = legjobb["gyakorlat"]
    ossz_kal_sorozat = osszes_kaloria_sorozat(gy)
    print(
        f"{gy['név']} - {ossz_kal_sorozat} kcal sorozatonként, {legjobb['sorozatok']} sorozat szükséges (összesen {legjobb['ossz_ismetles']} ismétlés) "
    )


if __name__ == "__main__":
    main()

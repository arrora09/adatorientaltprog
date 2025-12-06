def main():
    try:
        with open("posztok.csv", "r", encoding="utf-8") as f:
            sorok = f.readlines()

        posztok = []
        for i in range(1, len(sorok)):
            sor = sorok[i].strip()
            if not sor:
                continue

            ertekek = sor.split(",")
            poszt = {
                "subreddit": ertekek[0],
                "cim": ertekek[1],
                "upvotes": int(ertekek[2]),
                "downvotes": int(ertekek[3]),
            }
            poszt["karma"] = poszt["upvotes"] - poszt["downvotes"]
            posztok.append(poszt)

        total_karma = sum(poszt["karma"] for poszt in posztok)

        subreddit_karma = {}
        for poszt in posztok:
            sr = poszt["subreddit"]
            if sr not in subreddit_karma:
                subreddit_karma[sr] = 0
            subreddit_karma[sr] += poszt["karma"]

        legjobb_subreddit = max(subreddit_karma.items(), key=lambda x: x[1])

        nepszeru_posztok = [p for p in posztok if p["karma"] > 100]

        top_3 = sorted(posztok, key=lambda x: x["karma"], reverse=True)[:3]

        print("=== Demonstrátor Úr Reddit Statisztikái ===")
        print()
        print(f"Összes karma: {total_karma}")
        print()
        print(
            f"Legjobban teljesítő subreddit: {legjobb_subreddit[0]} ({legjobb_subreddit[1]} karma)"
        )
        print()
        print(f"Népszerű posztok (karma > 100):")
        print(f"- {len(nepszeru_posztok)} poszt")
        print()
        print("Top 3 legjobb poszt:")
        for i, poszt in enumerate(top_3, 1):
            print(
                f'{i}. "{poszt["cim"]}" - {poszt["subreddit"]} - {poszt["karma"]} karma'
            )

    except FileNotFoundError:
        print("Hiba! A posztok.csv fájl nem található!")
    except Exception as e:
        print(f"Hiba! {e}")


if __name__ == "__main__":
    main()

def main():
    scores = dict()
    with open("scrabble_scores.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("-")
            scores[parts[0]] = int(parts[1])

    word = str(input("Adjon meg egy szot a Scrabble jatekhoz (vegjel: -): "))

    while word.strip() != "-":
        points = 0

        for c in word.strip():
            points += scores[c.upper()]

        print(points)

        word = str(input("Adjon meg egy szot a Scrabble jatekhoz (vegjel: -): "))


if __name__ == "__main__":
    main()

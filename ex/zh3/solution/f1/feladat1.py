def main():
    pass


if __name__ == "__main__":
    genres = dict()

    with open("books.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            parts = line.strip().split(";")

            genreList = parts[6].strip().split(", ")
            for g in genreList:
                if g in genres:
                    genres[g] += 1
                else:
                    genres[g] = 1
        for g in sorted(genres, key=str.lower):
            print(f"{g}: {genres[g]}")

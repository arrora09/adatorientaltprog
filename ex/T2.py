def helper(word):
    low = "aáoóuú"
    high = "eéiíöőöüű"
    bLow = False
    bHigh = False

    for c in word:
        if c in low:
            bLow = True
        elif c in high:
            bHigh = True

    if bLow and bHigh:
        return "vegyes"
    elif bLow and not bHigh:
        return "mély"
    elif not bLow and bHigh:
        return "magas"


def task2():
    with open("words.txt", "r", encoding="utf-8") as fin, open(
        "datas.txt", "w", encoding="utf-8"
    ) as fout:
        d = {"magas": 0, "mély": 0, "vegyes": 0}

        for l in fin:
            word = l.strip()
            category = helper(word)
            if category:
                d[category] += 1
        for e in d:
            fout.write(f"{e.capitalize()} hangrendű szavak - {d[e]}\n")


if __name__ == "__main__":
    task2()

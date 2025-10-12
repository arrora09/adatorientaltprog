MELY_MGHK = "aáoóuú"
MAGAS_MGHK = "eéiíöőüű"
words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]


def decide(s):
    high = False
    low = False
    for e in s:
        if e in MELY_MGHK:
            low = True
        elif e in MAGAS_MGHK:
            high = True

    if high and low:
        return "vegyes"
    elif high and not low:
        return "magas"
    elif not high and low:
        return "mély"
    else:
        return "semmilyen"


for e in words:
    print(e)
    print(decide(e))
    print()

def hamming(s1: str, s2: str) -> int | str:
    if len(s1) != len(s2):
        return "A hossz különböző, Hamming nem értelmezett"

    diffs = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diffs += 1

    return diffs


if __name__ == "__main__":
    print(hamming("asd", "dsa"))
    print(hamming("asd", "da"))
    print(hamming("görög", "török"))



def main():
    cnt = 0
    while True:
        cnt += 1
        if cnt == 42:
            break

    print(cnt)


    li = ["ananasz", "banan", "citrom"]

    for e in li:
        if e == "banan":
            continue
        print(e)


def palidnrome():
    pass # TODO...


main()
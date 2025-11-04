def task1():
    with open("pontok.txt", "r") as f:
        marks = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
        for l in f:
            parts = l.split()
            point = float(parts[1])
            if point < 2.0:
                marks["1"] += 1
            elif point < 2.5 and point >= 2.0:
                marks["2"] += 1
            elif point < 3.0 and point >= 2.5:
                marks["3"] += 1
            elif point < 3.5 and point >= 3.0:
                marks["4"] += 1
            elif point >= 3.5:
                marks["5"] += 1

        print(f"Egyes - {marks['1']}")
        print(f"Kettes - {marks['2']}")
        print(f"Hármas - {marks['3']}")
        print(f"Négyes - {marks['4']}")
        print(f"Ötös - {marks['5']}")


if __name__ == "__main__":
    task1()

#!/usr/bin/env python3


def generateFibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def main():
    with open("fib_config.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        min_val = int(lines[1].strip())

    fib_numbers = generateFibonacci(n)

    filtered = [num for num in fib_numbers if num >= min_val]

    print(f"Generált számok: {len(fib_numbers)} db")
    print(f"Szűrt számok: {len(filtered)} db")

    if filtered:
        total = sum(filtered)
        avg = total / len(filtered)
        print(f"Összeg: {total}")
        print(f"Átlag: {avg:.2f}")

    with open("fibonacci.txt", "w", encoding="utf-8") as outF:
        for num in filtered:
            outF.write(str(num) + "\n")

    print("-- fibonacci.txt was created")


if __name__ == "__main__":
    main()

import json


def main():
    with open("primes.json") as f:
        d = json.load(f)

        palindromes = []

        for n in d["primes"]:
            if str(n) == str(n)[::-1]:
                palindromes.append(n)
                print(n)

        print()
        print(len(palindromes))


if __name__ == "__main__":
    main()

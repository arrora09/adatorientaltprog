import json
from is_prime import is_prime_mr


def main():
    li = []
    for i in range(10000000):
        if is_prime_mr(i):
            li.append(i)

    d = dict()
    d["primes"] = li

    with open("primes.json", "w") as f:
        json.dump(d, f)


if __name__ == "__main__":
    main()

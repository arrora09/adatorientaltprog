#!/usr/bin/env python3

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with open("numbers.txt", "r", encoding="utf-8") as f:
        primes = []
        for line in f:
            num = int(line.strip())
            if isPrime(num):
                primes.append(num)
        
        primes.sort()
        
        print(f"Prímszámok: {', '.join(map(str, primes))}")
        print(f"Prímek összege: {sum(primes)}")

if __name__ == '__main__':
    main()

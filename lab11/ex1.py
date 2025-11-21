import is_prime as isp
from is_prime import is_prime_mr

if __name__ == "__main__":
    primes = [n for n in range(2, 100) if is_prime_mr(n)]
    print(primes)
    print(isp.hello())

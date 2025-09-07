import math

def solve():
    n, k = map(int, input().split())
    
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    small_primes = [i for i in range(2, n+1) if sieve[i]]
    
    def is_prime(x):
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        r = int(math.isqrt(x))
        for i in range(3, r+1, 2):
            if x % i == 0:
                return False
        return True
    
    count = 0
    candidate = 3
    while True:
        candidate += 1
        if is_prime(candidate):
            continue 
        ok = True
        for p in small_primes:
            if candidate % p == 0:
                ok = False
                break
        if ok:
            count += 1
            if count == k:
                print(candidate)
                return

if __name__ == "__main__":
    solve()
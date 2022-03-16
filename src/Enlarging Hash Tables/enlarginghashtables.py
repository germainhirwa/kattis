import sys

LIMIT = 40001
sieve = [True] * LIMIT
sieve[1] = False
primes = []

def prime(n):
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        if p == 2:
            p -= 1
        p += 2
    return True

for p in range(2, LIMIT):
    if sieve[p]:
        primes.append(p)
        for i in range(2*p, LIMIT, p):
            sieve[i] = False

for line in sys.stdin:
    k = int(line)
    if k == 0:
        break

    check = 2 * k + 1
    
    if check < LIMIT:
        lo, hi = 0, len(primes)
        while lo < hi:
            mid = (lo + hi) // 2
            if primes[mid] == check:
                break
            elif primes[mid] < check:
                lo = mid + 1
            else:
                hi = mid
        while primes[mid] < check:
            mid += 1
        print(primes[mid], end=' ')
        print(f'({k} is not prime)'*int(not sieve[k]))
    else:
        while not prime(check):
            check += 1
        if not prime(k):
            print(f'{check} ({k} is not prime)')
        else:
            print(check)
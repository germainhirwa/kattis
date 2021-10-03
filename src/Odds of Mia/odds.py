import sys

def wins(a, b, c, d):
    if a + b == 3:
        return int((c + d) != 3) # mia vs any, tie at mia
    elif c + d == 3:
        return 0 # any\mia vs mia
    elif a == b and c == d:
        return int(a > c) # pair vs pair
    elif a == b:
        return 1 # pair VS hc
    elif c == d:
        return 0 # hc VS pair
    else: # hc vs hc
        h1 = 10*max(a,b) + min(a,b)
        h2 = 10*max(c,d) + min(c,d)
        return int(h1 > h2)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for line in sys.stdin:
    a, b, c, d = line.strip().split(" ")
    if a + b + c + d == "0000":
        sys.exit(0)
    
    a, b, c, d = list(map(lambda x: list(range(1, 7)) if x == "*" else [int(x)], [a, b, c, d]))
    w, t = 0, 0
    for a1 in a:
        for b1 in b:
            for c1 in c:
                for d1 in d:
                    w += wins(a1, b1, c1, d1)
                    t += 1

    if 0 < w < t:
        print(f"{w//gcd(w,t)}/{t//gcd(w,t)}")
    else:
        print(w//t)
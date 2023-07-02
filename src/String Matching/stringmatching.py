import sys

t = 1
for l in sys.stdin:
    if t: P, t = l.strip(), 0
    else:
        T, t = l.strip(), 1
        n, m = len(T), len(P)
        b = [0]*(m+1)
        i, j = 0, -1
        b[0] = -1
        while i < m:
            while j >= 0 and P[i] != P[j]: j = b[j]
            i += 1; j += 1; b[i] = j
        i = j = 0
        matches = []
        while i < n:
            while j >= 0 and T[i] != P[j]: j = b[j]
            i += 1; j += 1
            if j == m: matches.append(i-m); j = b[j]
        print(*matches)
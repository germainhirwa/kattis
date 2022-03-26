import sys

for line in sys.stdin:
    s = line.strip()
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    ans = 1
    for i in range(2, len(s) + 1):
        ans *= i
    for v in freq.values():
        for k in range(2, v + 1):
            ans //= k
    print(ans)
n = int(input())
s = sorted(map(int, input().split()))
a, b = map(int, input().split())
best = (-1, -1)
for v in (a, b, *((s[i]+s[i+1])//2 for i in range(n-1))):
    if v % 2 == 0:
        v1, v2 = v-1, v+1
        if a <= v1 <= b: best = max(best, min((abs(v1-x), v1) for x in s))
        if a <= v2 <= b: best = max(best, min((abs(v2-x), v2) for x in s))
    elif a <= v <= b: best = max(best, min((abs(v-x), v) for x in s))
print(best[1])
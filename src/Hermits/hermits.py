n = int(input())
a = list(map(int, input().split()))
m = a.copy()
for _ in range(int(input())):
    l, r = map(lambda x: int(x)-1, input().split())
    m[l] += a[r]; m[r] += a[l]
print(min(enumerate(m), key=lambda x: x[::-1])[0]+1)
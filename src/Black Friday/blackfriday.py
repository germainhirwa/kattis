n = int(input())
a = list(map(int, input().split(" ")))
d = {}

for i in range(n):
    d[a[i]] = d.get(a[i], []) + [i]

try:
    print(max(filter(lambda x: len(x[1]) == 1, d.items()), key = lambda x: x[0])[1][0] + 1)
except:
    print("none")
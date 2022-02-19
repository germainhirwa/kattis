t = int(input())

arr = []
base = []
for _ in range(2001):
    found = False
    for i in range(len(base)):
        if base[i] == 0:
            found = True
            break
    if not found:
        base = list(map(lambda x: x-1, base)) + [len(base) + 1]
    else:
        base[i] = i + 1
        for j in range(i):
            base[j] -= 1
    arr.append(base.copy())

for _ in range(t):
    k, n = list(map(int, input().split()))
    b = arr[n - 1]
    print(k, len(b))
    for i in range(len(b) // 10 + 1):
        print(*b[10*i:10*(i+1)])
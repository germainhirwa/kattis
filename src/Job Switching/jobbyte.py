n, arr = int(input()), list(map(int, input().split()))
v, c = set(), []
for i in arr:
    if i not in v:
        cc = []
        while i not in v:
            v.add(i), cc.append(i)
            i = arr[i-1]
        c.append(cc)
print(sum(map(len, c))-len(c))
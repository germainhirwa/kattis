import sys; input = sys.stdin.readline
n, arr = int(input()), list(map(int, input().split()))
v, c = [0]*(n+1), []
for i in arr:
    if not v[i]:
        cc = []
        while not v[i]:
            v[i] = 1; cc.append(i)
            i = arr[i-1]
        c.append(cc)
print(sum(map(len, c))-len(c))
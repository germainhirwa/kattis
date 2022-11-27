n, k = map(int, input().split())
v = list(map(int, input().split()))
s = dict(map(reversed, enumerate(sorted(v))))

def lis(arr):
    def upper_bound(sub, idx):
        lo, hi = 0, len(sub) - 1
        while hi > lo:
            mid = (lo + hi) // 2
            if arr[sub[mid]] <= arr[idx]:
                lo = mid + 1
            else:
                hi = mid
        return hi

    temp = []
    par = [None] * len(arr)

    for i in range(len(arr)):
        if not temp or arr[i] >= arr[temp[-1]]:
            if temp:
                par[i] = temp[-1]
            temp.append(i)
        else:
            rep = upper_bound(temp, i)
            temp[rep] = i
            if rep != 0:
                par[i] = temp[rep - 1]

    final = []
    curr = temp[-1]
    while curr != None:
        final.append(curr)
        curr = par[curr]
    return len(final)

v2 = list(map(lambda x: s[x]//k, v))
print(n - lis(v2))
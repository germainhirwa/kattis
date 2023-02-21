n, arr = input(), list(map(int, input().split()))
arr2 = arr.copy()
arr = [(e, i) for i, e in enumerate(arr)]
first = max(arr)[1]
arr.pop(first)
tmp = [first] + [x[1] for x in sorted(arr)]
s = arr2[first]
if 2*s <= sum(arr2): print(*[x+1 for x in tmp])
else: print('impossible')
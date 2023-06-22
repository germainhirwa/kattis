arr = list(map(int, input().split()))
k = int(input())

def powerset(arr):
    ps = [[]]
    for i in arr:
        new_ps = []
        for j in ps:
            new_ps.append(j)
            new_ps.append(j+[i])
        ps = new_ps
    return ps

s = 0
for i in filter(lambda x: len(x) == k, powerset(range(10))):
    w = 1
    for j in i: w *= arr[j]
    s += w
print(s)
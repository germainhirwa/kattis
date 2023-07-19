from collections import Counter
n, a = int(input()), Counter(map(int, input().split()))
s = 0
for i, j in a.items():
    s += (i+1)*(j//(i+1))
    if a[i] > (i+1)*(j//(i+1)): s += i+1
print(s)
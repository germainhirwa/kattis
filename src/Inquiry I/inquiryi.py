import sys

input()
arr = []
for line in sys.stdin:
    arr.append(int(line))
sl, sr, m = 0, sum(arr), 0
for i in arr:
    sl += i**2
    sr -= i
    m = max(m, sl*sr)
print(m)
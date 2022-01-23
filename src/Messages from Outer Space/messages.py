import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())
k = lines.index('#')
words = lines[:k]
check = lines[k + 1:-1]

def max_kw(s):
    arr = []
    ans = 0
    for w in words:
        pos = s.find(w)
        while pos != -1:
            arr.append([pos, pos + len(w) - 1])
            pos = s.find(w, pos + 1)
    arr.sort(key=lambda x: x[1])
    hi = -1
    for a, b in arr:
        if a > hi:
            hi = b
            ans += 1
    return ans

temp = ''
for w in check:
    if w[-1] == '|':
        temp += w[:-1]
        print(max_kw(temp))
        temp = ''
    else:
        temp += w
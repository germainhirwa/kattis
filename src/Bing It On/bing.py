import sys
f = {}
input()
for w in sys.stdin:
    s = ''
    for i in w.strip():
        s += i
        if s not in f: f[s] = 0
        f[s] += 1
    print(f[s]-1)
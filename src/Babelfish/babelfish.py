import sys
h = {}
while True:
    s = sys.stdin.readline().strip()
    if not s: break
    a, b = s.split(); h[b] = a
for l in sys.stdin:
    l = l.strip()
    if l not in h: print('eh')
    else: print(h[l])
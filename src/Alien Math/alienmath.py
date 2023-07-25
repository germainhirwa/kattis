import sys; input = sys.stdin.readline
b, d, x = int(input()), input().strip().split(), input().strip()
r = {e:i for i,e in enumerate(d)}; a = 0
for i in sorted(d, key=len, reverse=True): x = x.replace(i, chr(r[i]+1000))
for i in x: a *= b; a += ord(i)-1000
print(a)
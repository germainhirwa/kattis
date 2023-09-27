import re, sys; input = sys.stdin.readline
p = input().strip().replace('.', '@').replace('*', '.*').replace('@', '\.')
for _ in range(int(input())):
    f = input().strip()
    if p == p[:3]*50 and p[-1].isalpha():
        if f.count(p[2]) >= 50 and p[-1] == f[-1]: print(f)
    elif f in re.findall(p, f): print(f)
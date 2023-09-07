import sys; input = sys.stdin.readline
s = input().strip()
r = [input().strip().split() for _ in range(int(input()))]
for _ in range(int(input())):
    p = input().strip(); ok = 0
    for rr in r:
        for r1 in rr:
            if p.endswith(r1):
                for r2 in rr:
                    if s.endswith(r2): ok = 1; break
            if ok: break
        if ok: break
    print('YNEOS'[1-ok::2])
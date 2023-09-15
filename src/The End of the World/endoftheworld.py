import sys; input = sys.stdin.readline
while (s:=input().strip()) != 'X':
    s = [*s]; ans = 0; base = 'B'
    while s:
        t = {*'ABC'}; t.discard(base)
        while s and s[-1] == base: s.pop()
        if s: t.discard(s[-1]); base = [*t][0]; ans += 1<<(len(s)-1); s.pop()
    print(ans)
from collections import deque
for t in range(int(input())):
    S, T = input().strip(), input().strip()
    a = b = c = d = ans = 0
    for i in range(len(S)):
        a += S[i] == '0' and T[i] == '1'
        b += S[i] == '1' and T[i] == '0'
        c += S[i] == '?' and T[i] == '0'
        d += S[i] == '?' and T[i] == '1'
    e = min(a, b); a -= e; b -= e; ans += e # 0s <-> 1s
    ans += a; a = 0 # 0 -> 1
    if b > d: ans = -1
    else: ans += b+c+d
    print(f'Case {t+1}:', ans)
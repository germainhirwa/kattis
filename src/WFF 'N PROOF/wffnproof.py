while True:
    s = input().strip(); ans = reserve = ''
    if s == '0': break
    p, q, r, s, t, K, A, N, C, E = [s.count(i) for i in 'pqrstKANCE']
    ans += 'N'*N
    if p: p -= 1; reserve = 'p'
    elif q: q -= 1; reserve = 'q'
    elif r: r -= 1; reserve = 'r'
    elif s: s -= 1; reserve = 's'
    elif t: t -= 1; reserve = 't'
    for ch, v in (('K', K), ('A', A), ('C', C), ('E', E)):
        for _ in range(v):
            if p: p -= 1; ans += ch+'p'
            elif q: q -= 1; ans += ch+'q'
            elif r: r -= 1; ans += ch+'r'
            elif s: s -= 1; ans += ch+'s'
            elif t: t -= 1; ans += ch+'t'
    print(ans+reserve if ans and reserve else 'no WFF possible')
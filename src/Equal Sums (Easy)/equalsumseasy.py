import sys; input = sys.stdin.readline
for T in range(int(input())):
    _, *A = map(int, input().split())
    H = {}
    for i in range(1, 1<<20):
        s = 0
        for j in range(20):
            if i&(1<<j): s += A[j]
        if s not in H: H[s] = []
        H[s].append(i)
    fd = False
    for i in H:
        for j in H[i]:
            for k in H[i]:
                if j&k == 0:
                    jj, kk = bin(j)[2:].zfill(20), bin(k)[2:].zfill(20)
                    L, R = [], []
                    for l in range(20):
                        if jj[19-l] == '1': L.append(A[l])
                        if kk[19-l] == '1': R.append(A[l])
                    print(f'Case #{T+1}:'), print(*L), print(*R); fd = True; break
            if fd: break
        if fd: break
    if not fd: print(f'Case #{T+1}:'), print('Impossible')
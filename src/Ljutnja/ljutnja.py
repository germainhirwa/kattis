import sys; input = sys.stdin.readline
M, N = map(int, input().split())
A = sorted(map(int, sys.stdin))

def check(K):
    M2 = M
    A2 = A.copy()
    i = N-1
    while i >= 0:
        if M2 == 0 or A2[i] <= K:
            for j in range(i+1, N):
                if M2 == 0: break
                A2[j] -= 1; M2 -= 1
            break
        D = min(A2[i]-K, M2)
        M2 -= D; A2[i] -= D
        i -= 1
    return [M2 == 0, A2]

lo, hi = A[0], A[-1]
while abs(lo-hi) > 1:
    K = (lo+hi)//2
    if check(K)[0]: lo = K
    else: hi = K-1
for i in range(hi+1, lo-2, -1):
    c = check(i)
    if c[0]: print(sum(i**2 for i in c[1])), exit(0)
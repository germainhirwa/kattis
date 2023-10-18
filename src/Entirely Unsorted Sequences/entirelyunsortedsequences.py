from collections import *
from array import *
import sys; input = sys.stdin.readline
F = array('i', [1]); C = Counter(); MOD = 10**9+9; fact = array('i', [1]); P = array('i', [1]); n = int(input()); a = array('i', sorted(map(int, input().split()))); inv = array('i', [0])
for i in range(n): fact.append(fact[-1]*(i+1)%MOD); inv.append(pow(i+1, -1, MOD))
for k in range(1, n+1):
    f = F[-1]*k%MOD*inv[C[a[k-1]]+1]%MOD; C[a[k-1]] += 1; F.append(f); v = f
    for i in range(k): f *= C[a[i]]*inv[k-i]; C[a[i]] -= 1; f %= MOD; v -= P[i]*f; v %= MOD
    for i in range(k): C[a[i]] += 1
    P.append(v)
print(P[-1])
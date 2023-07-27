import sys; input = sys.stdin.readline
def gcd(a, b):
    while b: a, b = b, a % b
    return a
A = [int(input()) for _ in range(int(input()))]; G = [{A[0]}]
for i in range(1, len(A)): G.append({A[i], *(gcd(j, A[i]) for j in G[-1])}); G[0] |= G[-1]
print(len(G[0]))
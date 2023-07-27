import sys; input = sys.stdin.readline
S = [int(input()) for _ in range(int(input()))]; H = {i:i for i in S}
for D in range(60):
    for i in S:
        if i&(1<<D): # just swap with any of its submask
            j = i-(1<<D); H[i], H[j] = H[j], H[i]
sys.stdout.write('\n'.join(str(H[i]) for i in S))
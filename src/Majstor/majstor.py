R = int(input()); Y = input(); N = int(input()); RPS = [input() for _ in range(N)]
S = {'RS': 2, 'RR': 1, 'RP': 0, 'PR': 2, 'PP': 1, 'PS': 0, 'SP': 2, 'SS': 1, 'SR': 0}
ss, best = 0, 0
for rps in RPS:
    for i, j in zip(Y, rps): ss += S[i+j]
for i in range(R):
    bb = 0
    for t in 'RPS': bb = max(bb, sum(S[t+rps[i]] for rps in RPS))
    best += bb
print(ss)
print(best)
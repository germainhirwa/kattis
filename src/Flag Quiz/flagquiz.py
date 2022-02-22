import sys

q = input()
n = int(input())

alts = []
for line in sys.stdin:
    line = line.strip().split(', ')
    alts.append(line)
kk = len(alts[0])

score = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        sc = 0
        for k in range(kk):
            if alts[i][k] != alts[j][k]:
                sc += 1
        score[i] = max(score[i], sc)
        score[j] = max(score[j], sc)
best = min(score)
for i in range(n):
    if score[i] == best:
        print(', '.join(alts[i]))
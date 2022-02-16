import sys, itertools
skip = input()

tries = []
for line in sys.stdin:
    tries.append(list(map(lambda x: int(x == 'T'), line.strip())))

n = len(tries[0])
gen = list(itertools.product(*[[0, 1]] * n))
ans = 0
for comb in gen:
    temp = n
    for t in tries:
        temp = min(temp, sum(map(lambda x: t[x] == comb[x], range(n))))
    ans = max(ans, temp)
print(ans)
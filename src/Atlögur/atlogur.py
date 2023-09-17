n = int(input()); w = [[*map(int, input().split())] for _ in range(n)]; s, t = 0, 1
for _ in range(n-1):
    hi, di = w[s]; hj, dj = w[t]; wi, wj = (hj+di-1)//di, (hi+dj-1)//dj
    if wi <= wj: w[s][0] -= (wi-1)*dj; s, t = s, t+1
    else: w[t][0] -= wj*di; s, t = t, t+1
print(s+1)
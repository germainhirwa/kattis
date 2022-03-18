dp = []
for l in range(41):
    dp.append([0] * 1001)
for c in range(1, 27):
    dp[1][c] = c
for l in range(40):
    for c in range(1, 27):
        for k in range(975):
            if dp[l][k] != 0:
                dp[l + 1][k + c] = dp[l][k] * 27 + c
                
l, k = map(int, input().split())
h = dp[l][k]
if h == 0:
    print('impossible')
else:
    while h != 0:
        print(chr(h % 27 + 96), end='')
        h //= 27
def dp(s, t='welcome to code jam'):
    arr = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
    for j in range(len(s)+1): arr[0][j] = 1
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            arr[i][j] = arr[i][j-1] + arr[i-1][j-1]*(s[j-1] == t[i-1])
    return str(arr[len(t)][len(s)] % 10**4)
for c in range(int(input())): print(f'Case #{c+1}: {dp(input()).zfill(4)}')
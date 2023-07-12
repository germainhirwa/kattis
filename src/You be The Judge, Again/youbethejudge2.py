from collections import defaultdict
n = int(input())
m = 1<<n
grid = [[*map(int, input().split())] for _ in range(m)]
ctr = defaultdict(int)
for i in range(m):
    for j in range(m):
        if i > 0:
            if j > 0 and grid[i][j] == grid[i-1][j] == grid[i][j-1]: ctr[grid[i][j]] += 1
            if j < m-1 and grid[i][j] == grid[i-1][j] == grid[i][j+1]: ctr[grid[i][j]] += 1
        if i < m-1:
            if j > 0 and grid[i][j] == grid[i+1][j] == grid[i][j-1]: ctr[grid[i][j]] += 1
            if j < m-1 and grid[i][j] == grid[i+1][j] == grid[i][j+1]: ctr[grid[i][j]] += 1
print(int(len(ctr) == sum(ctr.values()) == (4**n-1)//3 and min(ctr) == 1 and max(ctr) == (4**n-1)//3))
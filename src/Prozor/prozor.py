import sys

first_line = False
grid = []
swats = []

for line in sys.stdin:
    if not first_line:
        a,b,c = list(map(int,line.split()))
        first_line = True
    else:
        grid.append(list(line.strip()))
        swats.append(([0]*b).copy())

maxI, maxJ, maxSwats = 0,0,0
for i in range(a-c+1):
    for j in range(b-c+1):
        swat = 0
        for k in range(1,c-1):
            for l in range(1,c-1):
                if grid[i+k][j+l] == "*":
                    swat += 1
        if swat > maxSwats:
            maxSwats = swat
            maxI, maxJ = i,j

print(maxSwats)
for i in range(1,c-1):
    grid[maxI][maxJ+i] = "-"
    grid[maxI+c-1][maxJ+i] = "-"
    grid[maxI+i][maxJ] = "|"
    grid[maxI+i][maxJ+c-1]  = "|"
grid[maxI][maxJ] = "+"
grid[maxI+c-1][maxJ] = "+"
grid[maxI][maxJ+c-1] = "+"
grid[maxI+c-1][maxJ+c-1] = "+"

for r in grid:
    print("".join(r))
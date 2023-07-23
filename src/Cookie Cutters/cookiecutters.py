n = int(input()); poly = [[*map(float, input().split())] for _ in range(n)]; a = 0
for i in range(n): a += poly[i][0]*poly[(i+1)%n][1] - poly[i][1]*poly[(i+1)%n][0]
scale = (2*int(input())/abs(a))**0.5
poly = [[x*scale, y*scale] for x, y in poly]
mx, my = min(p[0] for p in poly), min(p[1] for p in poly)
poly = [[x-mx, y-my] for x, y in poly]
for x, y in poly: print(x, y)
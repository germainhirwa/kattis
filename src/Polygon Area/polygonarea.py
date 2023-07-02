def area(poly):
    a, n = 0, len(poly)
    for i in range(n): a += poly[i][0]*poly[(i+1)%n][1] - poly[i][1]*poly[(i+1)%n][0]
    return a/2
while True:
    if not (n:=int(input())): break
    a = area([[*map(int, input().split())] for _ in range(n)])
    print(['CW', 'CCW'][a>0], abs(a))
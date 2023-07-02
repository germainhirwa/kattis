pts = sorted(list(map(float, input().split())) for _ in range(int(input())))
print(max(abs((pts[i][1]-pts[i+1][1])/(pts[i][0]-pts[i+1][0])) for i in range(len(pts)-1)))
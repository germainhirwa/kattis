import sys, math

for line in sys.stdin:
    r,x,y = list(map(float,line.split()))
    d = x**2 + y**2
    if d > r**2:
        print("miss")
    else:
        angle = math.acos(math.sqrt(d)/r)
        a1 = (math.pi-angle)*(r**2)+r*math.sqrt(d)*math.sin(angle)
        a2 = math.pi*(r**2)-a1
        print(max(a1,a2),min(a1,a2))
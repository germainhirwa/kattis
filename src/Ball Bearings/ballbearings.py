import sys, math

for line in sys.stdin:
    try:
        D,d,s = list(map(float,line.split()))
        print(int(math.pi/math.asin((s+d)/(D-d))))
    except:
        pass
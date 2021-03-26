import sys

for line in sys.stdin:
    k = len(line)//3
    line = [line[k*i:k*(i+1)] for i in range(3)]
    d = {}
    for w in line:
        d[w] = d.get(w,0)+1
    if d[line[0]] > 1:
        print(line[0])
    else:
        print(line[1])
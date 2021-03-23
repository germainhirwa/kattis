import sys

for line in sys.stdin:
    line = list(map(int,line.split(" ")))[1:]
    checks = [False]*(len(line)-1)
    jolly = True
    for i in range(1,len(line)):
        if not 1 <= abs(line[i]-line[i-1]) <= len(line)-1:
            jolly = False
            break
        elif checks[abs(line[i]-line[i-1])-1]:
            jolly = False
            break
        else:
            checks[abs(line[i]-line[i-1])-1] = True
    
    for i in range(len(line)-1):
        if not checks[i]:
            jolly = False
            break
    
    if jolly:
        print('Jolly')
    else:
        print('Not jolly')
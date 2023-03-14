import sys
for line in [input(), sys.stdin][1]:
    line = line.strip('\r\n')
    for i in range(len(line)):
        s = line[:i+1]
        k = len(line)//(i+1) + 1
        if (s*k).startswith(line):
            print(i+1); break
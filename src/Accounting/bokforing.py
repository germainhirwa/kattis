import sys

skip = input()
default = 0
mem = {}

for line in sys.stdin:
    line = line.split()
    if line[0] == 'SET':
        mem[int(line[1])] = int(line[2])
    elif line[0] == 'PRINT':
        print(mem.get(int(line[1]), default))
    else:
        mem = {}
        default = int(line[1])
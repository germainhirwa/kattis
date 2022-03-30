import sys

pc = [-1, -1, -1, -1, -1]
t = [0, 0, 0, 0, 0]
mul = [9, 4, 4, 4, 7]
for line in sys.stdin:
    line = line.strip().split()
    if line == ['-']:
        if sum(t) != 0:
            print(f'{round(t[0] / sum(t) * 100)}%')
            t = [0, 0, 0, 0, 0]
        continue

    pc = [-1, -1, -1, -1, -1]
    for i in range(5):
        if line[i][-1] == 'g':
            line[i] = int(line[i][:-1]) * mul[i]
        elif line[i][-1] == 'C':
            line[i] = int(line[i][:-1])
        else:
            pc[i] = int(line[i][:-1])
    curr_pc = 100 - sum([i for i in pc if i != -1])
    
    cal = 0
    for i in range(5):
        if pc[i] == -1:
            cal += line[i]
    cal_pc = cal / curr_pc

    for i in range(5):
        if type(line[i]) == str and line[i][-1] == '%':
            line[i] = cal_pc * int(line[i][:-1])
    
    for i in range(5):
        t[i] += line[i]
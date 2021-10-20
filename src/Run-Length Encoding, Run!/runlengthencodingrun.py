import sys

for line in sys.stdin:
    cmd = line.strip().split()

    if cmd[0] == "E":
        prev, prev_idx = cmd[1][0], 0
        for i in range(len(cmd[1])):
            if cmd[1][i] != prev:
                print(prev+str(i-prev_idx), end = "")
                prev, prev_idx = cmd[1][i], i
        print(cmd[1][-1]+str(len(cmd[1])-prev_idx))
    else: # cmd[0] == "D"
        for i in range(len(cmd[1])//2):
            print(cmd[1][2*i]*int(cmd[1][2*i+1]), end = "")
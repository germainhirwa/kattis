import sys
n = input() # don't need
for line in sys.stdin:
    seq = list(map(int, line.split()))
    l = seq[0]
    arithmetic = True
    d = seq[2] - seq[1]
    for i in range(1, l):
        if seq[i + 1] - seq[i] != d:
            arithmetic = False
            break

    if arithmetic:
        print("arithmetic")
    else:
        tmp = sorted(seq[1:])
        perm_arithmetic = True
        d = tmp[1] - tmp[0]
        for i in range(l - 1):
            if tmp[i + 1] - tmp[i] != d:
                perm_arithmetic = False
                break
        if perm_arithmetic:
            print("permuted arithmetic")
        else:
            print("non-arithmetic")
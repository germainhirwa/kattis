import sys

fl = []

def do():
    for line in sys.stdin:
        if not fl:
            fl.extend(list(map(int,line.split())))
        else:
            arr = list(map(int,line.split()))
            arr.sort()
            for i in range(1,fl[0]):
                if arr[i]+arr[i-1] > fl[1]:
                    print(i)
                    return
            print(fl[0])

do()

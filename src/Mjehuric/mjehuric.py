import sys

for line in sys.stdin:
    lst = line.strip().split(" ")
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j+1],lst[j] = lst[j],lst[j+1]
                print(" ".join(lst))
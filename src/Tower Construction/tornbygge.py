import sys

fl = True
for line in sys.stdin:
    if fl:
        fl = False
    else:
        ans = 1
        lst = list(map(int,line.split(" ")))
        for i in range(1,len(lst)):
            if lst[i] > lst[i-1]:
                ans += 1
        print(ans)
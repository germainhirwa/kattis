from heapq import *
import sys; input = sys.stdin.readline
for _ in range(int(input())):
    bq = []; sq = []; r = '-'
    for _ in range(int(input())):
        o, x, _, _, y = input().split(); x, y = int(x), int(y)
        if o[0] == 'b': [heappush(bq, -y) for _ in '.'*x]
        else: [heappush(sq, y) for _ in '.'*x]
        while bq and sq and -bq[0] >= sq[0]: heappop(bq); r = heappop(sq)
        print(sq[0] if sq else '-', -bq[0] if bq else '-', r)
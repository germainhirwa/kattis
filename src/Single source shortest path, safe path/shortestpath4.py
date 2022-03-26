from heapq import *
import sys

for _ in range(int(input())):
    input() # skip newline
    v = int(input())
    v2 = v**2
    g = [None]*v

    cnt = 0
    for line in sys.stdin:
        arr = list(map(int, line.split()))
        g[cnt] = []
        for i in range(arr[0]):
            g[cnt].append((arr[2*i + 1], arr[2*i + 2]))
        cnt += 1
        if cnt == v:
            break

    q = int(input())

    for line in sys.stdin:
        q -= 1
        s, t, k = map(int, line.split())
        
        if s != t and k < 2:
            print(-1)
        elif s == t:
            print(0)
        else:
            # Need to separate into a k*v array instead of a 1*v array
            # We might update the shortest path to that node when the remaining junctions
            # are different if we use a 1*v array which doesn't make sense
            D = []
            for _ in range(k):
                temp = [10**9] * v
                temp[s] = 0
                D.append(temp)
            
            pq = [0*v2 + (k-1)*v + s]
            ans = -1

            while pq:
                h = heappop(pq)
                dd, left, vv = h // v2, h // v % v, h % v
                if vv == t:
                    ans = dd
                    break
                if left > 0 and dd == D[left][vv]:
                    for nn, ww in g[vv]:
                        if D[left - 1][nn] > dd + ww:
                            D[left - 1][nn] = dd + ww
                            heappush(pq, (D[left - 1][nn]*v2 + (left - 1)*v + nn))
            print(ans)
        
        if q == 0:
            break
    print()
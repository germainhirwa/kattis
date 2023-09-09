from heapq import *
import sys; input = sys.stdin.readline
n, m, k = map(int, input().split()); q1 = [('Jane Eyre', k)]; q2 = []
for _ in range(n): _, b, t = input().split('"'); t = int(t); q1.append((b, t))
for _ in range(m): g, b, t = input().split('"'); t = int(t); g = int(g); q2.append((g, b, t))
heapify(q1), heapify(q2); tt = 0
while 1:
    while q2 and q2[0][0] <= tt: _, b, t = heappop(q2); heappush(q1, (b, t))
    b, t = heappop(q1); tt += t
    if b == 'Jane Eyre': print(tt); break
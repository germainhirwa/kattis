import sys; input = sys.stdin.readline
c = [*map(int, input().strip())]
w = [input().strip() for _ in range(int(input()))]
for i in w: print(''.join(chr((ord(e)-65)*c[j]%26+65) for j, e in enumerate(i)))
import sys; input = sys.stdin.readline
while True:
    n = int(input())
    if not n: break
    print(max([input().strip() for _ in range(n)], key=lambda x: sum(x.count(i*2) for i in 'aeiouy')))
import sys; input = sys.stdin.readline
n = int(input())
prev = input().strip()
mem = {prev}
for i in range(n - 1):
    w = input().strip()
    if w[0] == prev[-1] and w not in mem:
        prev = w
        mem.add(w)
    else:
        print(['Player 2 lost', 'Player 1 lost'][i % 2])
        sys.exit(0)
print('Fair Game')
import sys; input = sys.stdin.readline
N = int(input()); a, b = [], []
for _ in range(N): x, y = map(int, input().split()); a.append(x+y), b.append(x-y)
print(4+max(a)+max(b)-min(a)-min(b)+(N > 1 and (len({*a})==1 or len({*b})==1)))
n, p, m = map(int, input().split())
h = {input(): 0 for _ in range(n)}
w = set()
for _ in range(m):
    a, b = input().split(); h[a] += int(b)
    if h[a] >= p and a not in w: print(a, 'wins!'), w.add(a)
if not w: print('No winner!')
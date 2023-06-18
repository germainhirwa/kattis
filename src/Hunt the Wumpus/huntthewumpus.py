import sys

s = int(input())
w = set()
while len(w) != 4:
    s += s//13 + 15
    w.add(s%100)
for i, g in enumerate(sys.stdin):
    g = int(g)
    if g in w:
        print('You hit a wumpus!')
        w.discard(g)
    if w: print(min(map(lambda x: abs(x//10-g//10)+abs(x%10-g%10), w)))
    else: print(f'Your score is {i+1} moves.')
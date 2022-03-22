import sys

x, y = map(int, input().split())
input()

moves = []
for line in sys.stdin:
    moves.append(line.strip())

def simulate(moves):
    x, y, dx, dy = 0, 0, 0, 1
    for move in moves:
        if move == 'Forward':
            x += dx
            y += dy
        elif move == 'Left':
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx
    return (x, y)

for i in range(len(moves)):
    for check in ['Forward', 'Left', 'Right']:
        if check != moves[i]:
            if (x, y) == simulate(moves[:i] + [check] + moves[i+1:]):
                print(i + 1, check)
                sys.exit(0)
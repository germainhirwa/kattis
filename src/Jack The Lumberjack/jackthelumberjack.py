n = int(input())
yisb = []
for _ in range(n):
    yisb.append(list(map(int, input().split())))

ans = 0
for y, i, s, b in yisb:
    trees = 0
    # greedily check for b + y
    p = b + y
    for yy, ii, ss, bb in yisb:
        if bb <= p <= bb + yy:
            trees += ss + ii * (p - bb)
        elif bb + yy < p:
            trees += max(ss + ii * (2 * yy - (p - bb)), 0)
    ans = max(ans, trees)

print(ans)
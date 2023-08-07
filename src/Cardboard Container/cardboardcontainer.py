v = int(input())
best = 1e9
for l in range(1, int(v**0.5)+1):
    for w in range(1, int(v**0.5)+1):
        if v % (l*w) == 0:
            h = v//l//w
            best = min(best, 2*(l*w+w*h+h*l))
print(best)
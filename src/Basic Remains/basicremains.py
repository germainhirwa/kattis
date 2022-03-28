import sys

for line in sys.stdin:
    bpm = list(map(int, line.split()))
    if len(bpm) == 1:
        break
    b, p, m = bpm
    p, m = str(p), str(m)
    mod = int(p, b) % int(m, b)
    conv = []
    if not mod:
        print(0)
        continue
    while mod:
        conv.append(mod % b)
        mod //= b
    for i in range(len(conv) - 1, -1, -1):
        print(conv[i], end='')
    print()
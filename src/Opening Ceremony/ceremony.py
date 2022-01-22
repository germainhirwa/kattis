skip = input()
n = list(map(int, input().split()))
n.sort(reverse=True)

s, cp = 0, 0
while len(n) > cp:
    if cp < len(n) and len(n) - cp > n[cp]:
        # minus 1 and throw all 0's
        for i in range(cp, len(n)):
            n[i] -= 1
        while n and n[-1] == 0:
            n.pop()
    else:
        # throw max element
        cp += 1
    s += 1
print(s)
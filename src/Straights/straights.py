n = int(input())
arr = list(map(int, input().split()))
lo, hi = min(arr), max(arr)

deck = [0] * (10**4 + 1)
for i in arr:
    deck[i] += 1

s = 0
stack = []
while n != 0:
    for i in range(lo, hi + 1):
        if (not stack or stack[-1] == i - 1) and deck[i]:
            deck[i] -= 1
            n -= 1
            stack.append(i)
        else:
            if stack:
                s += 1
                stack.clear()
    if stack:
        s += 1
        stack.clear()
print(s)
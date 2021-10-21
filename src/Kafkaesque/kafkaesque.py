n = int(input())

import sys

arr = []
for line in sys.stdin:
    arr.append(int(line))

sort = sorted(arr)
ans = 0
cp = 0

while cp != n:
    for i in range(n):
        if cp == n:
            print(ans + 1)
            sys.exit(0)
        if sort[i] == arr[cp]:
            cp += 1
    ans += 1

print(ans)
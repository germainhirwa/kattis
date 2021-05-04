import sys

case = 1
for line in sys.stdin:
    a,b = list(map(int,line.split(" ")))
    ans = 0
    while (ans+a) % 365 or (ans+b) % 687:
        ans += 1
    print(f"Case {case}: {ans}")
    case += 1
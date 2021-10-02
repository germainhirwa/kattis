low = 0
high = int(input())
step = 1
print((low + high)//2, flush = True)

import sys
while True:
    verdict = input()
    step += 1
    if verdict == "less":
        high = (low + high)//2 - 1
    elif verdict == "more":
        low = (low + high)//2 + 1
    else:
        sys.exit(0)
    low *= step/(step-1)
    high *= step/(step-1)
    print(int((low + high)/2), flush = True)
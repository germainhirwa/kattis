skip = input()
import sys

arr = []
for line in sys.stdin:
    temp = int(line)
    if not arr or temp % arr[0] != 0:
        arr.append(temp)
    else:
        print(temp)
        arr.clear()
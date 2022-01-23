skip = input()
import sys

intervals = []
for line in sys.stdin:
    intervals.append(list(map(int, line.split())))
intervals.sort(reverse=True)

output = []
lo, hi = intervals.pop()
while intervals:
    interval = intervals.pop()
    if interval[0] <= hi:
        lo, hi = interval[0], min(hi, interval[1])
    else:
        output.append([lo, hi])
        lo, hi = interval
output.append([lo, hi])
print(len(output))
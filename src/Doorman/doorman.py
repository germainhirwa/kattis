import sys
x = int(input())
diff = 0
line = input()
for i, p in enumerate(line):
    diff += 2*int(p == 'M') - 1
    if abs(diff) > x + 1:
        print(i - 1)
        sys.exit(0)
if abs(diff) > x:
    print(len(line) - 1)
else:
    print(len(line))
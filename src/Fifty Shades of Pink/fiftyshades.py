import sys

first_line = False
ans = 0
for line in sys.stdin:
    if not first_line:
        first_line = True
    else:
        line = line.lower()
        ans += int("rose" in line or "pink" in line)

if ans:
    print(ans)
else:
    print("I must watch Star Wars with my daughter")
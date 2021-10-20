import sys

for line in sys.stdin:
    try:
        l = int(line)-1
        rooms[l] = True
    except:
        rooms = [False]*list(map(int,line.split()))[0]

for i in range(len(rooms)):
    if not rooms[i]:
        print(i+1)
        sys.exit(0)

print("too late")
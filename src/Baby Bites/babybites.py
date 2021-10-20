import sys

fl = True
for line in sys.stdin:
    if fl:
        fl = False
    else:
        fishy = False
        words = line.strip().split()
        for i in range(len(words)):
            if words[i] != "mumble" and int(words[i]) != i+1:
                fishy = True
                break
        print("something is fishy") if fishy else print("makes sense")
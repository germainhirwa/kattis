import sys

for line in sys.stdin:
    try:
        member = True
        n = float(line)
        for i in range(1,10):
            if n >= 2/(3**i):
                n -= 2/(3**i)
            elif n >= 1/(3**i):
                member = False
                break
        if member:
            print("MEMBER")
        else:
            print("NON-MEMBER")
    except:
        pass
import sys

for line in sys.stdin:
    a, b, c, d = list(map(int, line.split(" ")))
    if a + b + c + d == 0:
        sys.exit(0)
    
    if a + b == 3:
        if c + d == 3:
            print("Tie.")
        else:
            print("Player 1 wins.")
    elif c + d == 3:
        print("Player 2 wins.")
    elif a == b and c == d:
        if a > c:
            print("Player 1 wins.")
        elif a < c:
            print("Player 2 wins.")
        else:
            print("Tie.")
    elif a == b:
        print("Player 1 wins.")
    elif c == d:
        print("Player 2 wins.")
    else:
        h1 = 10*max(a,b) + min(a,b)
        h2 = 10*max(c,d) + min(c,d)
        if h1 > h2:
            print("Player 1 wins.")
        elif h1 < h2:
            print("Player 2 wins.")
        else:
            print("Tie.")
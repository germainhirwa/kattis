p, q = map(int, input().split())

if p % 2 and q % 2:
    print(1)
elif p % 2 == 0:
    print(0)
elif q > p:
    print(2)
else:
    print(0)
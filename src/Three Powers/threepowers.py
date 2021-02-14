n = -1
while n:
    n = int(input())
    if n == 0:
        break
    bins = list(bin(n-1)[2:])
    threes = []
    for i in range(len(bins)):
        if bins[i] == '1':
            threes.append(str(3**(len(bins)-1-i)))
    print("{ "+", ".join(threes[::-1])+" }")
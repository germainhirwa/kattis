n = int(input())
if n > 25: print(0), exit(0)
luck = [*range(1, 10)]
for k in range(n-1):
    luck2 = []
    for d in range(10):
        for l in luck:
            if (10*l+d)%(k+2) == 0: luck2.append(10*l+d)
    luck = luck2
print(len(luck))
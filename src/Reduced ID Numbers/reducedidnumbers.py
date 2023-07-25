C = [int(input()) for _ in range(int(input()))]
for i in range(1, 10**6):
    if len({m%i for m in C}) == len(C): print(i); break
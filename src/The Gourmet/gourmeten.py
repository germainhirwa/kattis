m = int(input())
arr = [int(input()) for _ in range(int(input()))]
mem = {}

def ways(m, arr):
    if m < 0: return 0
    if m == 0: return 1
    if m in mem: return mem[m]
    mem[m] = sum(ways(m-i, arr) for i in arr)
    return mem[m]

print(ways(m, arr))
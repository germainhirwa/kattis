t = int(input())
for _ in range(t):
    input()
    input()
    g = max(map(int, input().split()))
    mg = max(map(int, input().split()))
    print(['Godzilla', 'MechaGodzilla'][int(mg > g)])
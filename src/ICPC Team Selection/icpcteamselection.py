for _ in range(int(input())):
    n, a = int(input()), sorted(map(int, input().split()))
    print(sum(a[-2::-2][:n]))
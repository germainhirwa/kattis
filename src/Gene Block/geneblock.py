t = int(input())
mapper = {0:10, 1:3, 2:6, 3:9, 4:2, 5:5, 6:8, 7:1, 8:4, 9:7}
for _ in range(t):
    n = int(input())
    if n < 7 * mapper[n % 10]:
        print(-1)
    else:
        print(mapper[n % 10])
import sys; input = sys.stdin.readline
for _ in range(int(input())):
    t, d = input().split()
    p, q = map(int, d.split('/'))
    print(t, f'{q}/{(2*(p//q)+1)*q-p}')
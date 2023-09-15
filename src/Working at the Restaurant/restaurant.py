import sys; input = sys.stdin.readline
while (n:=int(input())):
    s1 = s2 = 0
    for _ in range(n):
        op, k = input().split(); k = int(k)
        if op == 'DROP': s2 += k; print(op, 2, k)
        else:
            if s1 >= k: s1 -= k; print(op, 1, k)
            else:
                if s1: print(op, 1, s1); k -= s1; s1 = 0
                print('MOVE 2->1', s2); s1, s2 = s2, 0; print(op, 1, k); s1 -= k
    print()
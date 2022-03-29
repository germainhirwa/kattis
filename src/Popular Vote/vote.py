for _ in range(int(input())):
    n = int(input())
    s, m, l = 0, 0, []
    for i in range(n):
        k = int(input())
        s += k
        if k > m:
            m = k
            l = [i]
        elif k == m:
            l.append(i)
    if len(l) != 1:
        print('no winner')
    elif m > s // 2:
        print('majority winner', l[0] + 1)
    else:
        print('minority winner', l[0] + 1)
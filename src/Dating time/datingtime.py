from bisect import *
a0 = [*range(0, 15840, 720)]
a90 = [*range(180, 15840, 360)]
a180 = [*range(360, 15840, 720)]
for _ in range(int(input())):
    t1, t2, a = input().split()
    (h1, m1), (h2, m2) = t1.split(':'), t2.split(':')
    s1 = 11*(60*int(h1)+int(m1))
    s2 = 11*(60*int(h2)+int(m2))
    a = int(a)
    if a == 0: a = a0
    elif a == 90: a = a90
    else: a = a180
    print(bisect_right(a, s2) - bisect_left(a, s1))
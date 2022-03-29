for _ in range(int(input())):
    print(input())
    s = input()
    print(s)
    n = int(s.split()[0])
    make = [0] * 10
    while n:
        temp = input().split()
        if len(temp) == 1:
            for i in temp[0]:
                make[int(i)] += 1
            n -= 1
        else:
            a, b, d = map(int, temp[1:])
            for i in range(a, b + 1, d):
                for j in str(i):
                    make[int(j)] += 1
                n -= 1
    for i in range(10):
        print('Make', make[i], 'digit', i)
    ss = sum(make)
    print('In total', ss, 'digit' + 's' * int(ss > 1))
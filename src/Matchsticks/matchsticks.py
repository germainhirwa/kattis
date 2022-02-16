import sys
skip = input()

small = {
    2: 1,
    3: 7,
    4: 4,
    5: 2,
    6: 6,
    7: 8,
    8: 10,
    9: 18,
    10: 22,
    11: 20,
    12: 28,
    13: 68,
    17: 200
}

for line in sys.stdin:
    n = int(line)
    if n in small:
        print(small[n], end=' ')
    else:
        k = n % 7 + 7
        if k == 10:
            k += 7
        lead = small[k]
        pad = (n - k) // 7
        for _ in range(pad):
            lead = lead * 10 + 8
        print(lead, end=' ')

    if n % 2:
        print('7' + '1' * ((n - 3) // 2))
    else:
        print('1' * (n // 2))
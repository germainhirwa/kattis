fbi = {
    "0":0, "1":1, "2":2,
    "3":3, "4":4, "5":5,
    "6":6, "7":7, "8":8,
    "9":9, "A":10, "C":11,
    "D":12, "E":13, "F":14,
    "H":15, "J":16, "K":17,
    "L":18, "M":19, "N":20,
    "P":21, "R":22, "T":23,
    "V":24, "W":25, "X":26
}

def check(s):
    c = [2, 4, 5, 7, 8, 10, 11, 13]
    v = 0
    for i in range(8):
        v += fbi[s[i]]*c[i]
    
    if v % 27 != fbi[s[-1]]:
        return "Invalid"
    else:
        t = 0
        for i in range(8):
            t *= 27
            t += fbi[s[i]]
        return t

n = int(input())
for _ in range(n):
    tc, s = input().strip().split()
    print(f"{tc} {check(s)}")
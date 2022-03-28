for _ in range(int(input())):
    c, dec = input().split()
    try:
        print(c, int(dec, 8), int(dec), int(dec, 16))
    except:
        print(c, 0, int(dec), int(dec, 16))
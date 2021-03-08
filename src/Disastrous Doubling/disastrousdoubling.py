import sys

def main():
    first_line = False
    k = 1
    for line in sys.stdin:
        if not first_line:
            first_line = True
        else:
            lst = line.split(" ")
            for i in lst:
                k *= 2
                k -= int(i)
                if k < 0:
                    print("error")
                    return
            print(k % 1_000_000_007)

main()
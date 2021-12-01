import sys

bits = []
for line in sys.stdin:
    try:
        n = int(line)
        try:
            bits.append(bit)
        except:
            pass
        bit = ["?"]*32
    except:
        try:
            cmd, i, j = line.split()
            i, j = int(i), int(j)
        except:
            cmd, i = line.split()
            i = int(i)
        if cmd == "SET":
            bit[i] = 1
        elif cmd == "CLEAR":
            bit[i] = 0
        elif cmd == "AND":
            try:
                bit[i] = bit[i] & bit[j]
            except:
                if 1 in [bit[i], bit[j]] or [bit[i], bit[j]] == ["?", "?"]:
                    bit[i] = "?"
                else:
                    bit[i] = 0
        elif cmd == "OR":
            try:
                bit[i] = bit[i] | bit[j]
            except:
                if 0 in [bit[i], bit[j]] or [bit[i], bit[j]] == ["?", "?"]:
                    bit[i] = "?"
                else:
                    bit[i] = 1

for b in bits:
    print("".join(map(str, b[::-1])))
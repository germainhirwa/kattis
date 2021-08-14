import sys

reg = [0]*10
ram = []
pos = 0

for line in sys.stdin:
    ram.append(int(line))

while len(ram) != 1000:
    ram.append(0)

for i in range(10001):
    code, a, b = ram[pos]//100, ram[pos]//10%10, ram[pos]%10
    pos += 1

    if code == 1:
        break
    
    if code == 2:
        reg[a] = b
    elif code == 3:
        reg[a] = (reg[a]+b)%1000
    elif code == 4:
        reg[a] = (reg[a]*b)%1000
    elif code == 5:
        reg[a] = reg[b]
    elif code == 6:
        reg[a] = (reg[a]+reg[b])%1000
    elif code == 7:
        reg[a] = (reg[a]*reg[b])%1000
    elif code == 8:
        reg[a] = ram[reg[b]]
    elif code == 9:
        ram[reg[b]] = reg[a]
    elif code == 0 and reg[b] != 0:
        pos = reg[a]

print(i+1)

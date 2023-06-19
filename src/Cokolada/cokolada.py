k = int(input())
bits = bin(k)[2:]
b = 2**(len(bin(k-1))-2)
print(b, ('0'*(len(bin(b))-2-len(bits))+bits).rfind('1'))
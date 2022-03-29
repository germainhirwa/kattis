import sys

input()
for line in sys.stdin:
    string = list(map(lambda x: ord(x) - 96 if x != ' ' else 0, line[2:].strip('\r\n')))
    new = [string[0]]
    for i in range(1, len(string)):
        if line[0] == 'e':
            new.append((new[-1] + string[i]) % 27)
        else:
            new.append((string[i] - string[i - 1]) % 27)
    print(''.join(map(lambda x: chr(x + 96) if x != 0 else ' ', new)))
import sys

for line in sys.stdin:
    s = line.split(" ")
    name = []
    hr = []
    for e in s:
        try:
            k = float(e)
            hr.append(k)
        except:
            name.append(e)
    print(sum(hr)/len(hr),' '.join(name))
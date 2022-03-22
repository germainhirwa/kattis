import sys

words = []
for line in sys.stdin:
    if not line.strip():
        words.sort(key=lambda x: x[::-1])
        for w in words:
            print(w.rjust(max(map(len, words))))
        words.clear()
        print()
    else:
        words.append(line.strip())
words.sort(key=lambda x: x[::-1])
for w in words:
    print(w.rjust(max(map(len, words))))
import sys

words_full, results = [], set()

for line in sys.stdin:
    words = line.strip().split(" ")
    for w in words:
        words_full.append(w)
        
for a in words_full:
    for b in words_full:
        if a != b:
            results.add(a+b)

results = list(results)
results.sort()
for r in results:
    print(r)
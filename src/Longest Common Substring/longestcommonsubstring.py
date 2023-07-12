import sys; input = sys.stdin.readline
# brute-force works :')
words = [input().strip() for _ in range(int(input()))]
word = min(words, key=len)
candidates = {word[i:i+j] for i in range(len(word)) for j in range(1, len(word)+1)}
for i in words:
    for j in list(candidates):
        if j not in i: candidates.discard(j)
print(max(map(len, candidates), default=0))
from collections import defaultdict
import sys

n = int(input())
words = []

for line in sys.stdin:
    words.append(line.strip())
    if len(words) == n:
        break

words.sort(key=lambda x: (-len(x), x))
input()
t = int(input())

score_mapper = defaultdict(lambda: 0)
score_mapper.update({3:1, 4:1, 5:2, 6:3, 7:5, 8:11})

memo = {}

def solve(boggle, words):
    if str(boggle) in memo:
        return memo[str(boggle)]
    wm = defaultdict(lambda: [])
    for i in range(4):
        for j in range(4):
            wm[boggle[i][j]] = wm.get(boggle[i][j], []) + [(i, j)]
    mem, found = set(), set()
    def check(i, j, pos, word):
        if pos >= len(word) or not 0 <= i < 4 or not 0 <= j < 4 or (i, j) in mem:
            return
        if word[pos] == boggle[i][j]:
            mem.add((i, j))
            found.add(word[:pos+1])
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx * dy != dx + dy:
                        check(i + dx, j + dy, pos + 1, word)
            mem.remove((i, j))
    for word in words:
        for i, j in wm[word[0]]:
            if word not in found:
                check(i, j, 0, word)
    found = found & set(words)
    score = sum(map(lambda x: score_mapper[len(x)], found))
    best = min(found, key=lambda x: (-len(x), x))
    memo[str(boggle)] = score, best, len(found)
    return memo[str(boggle)]

for _ in range(t):
    boggle = []
    for _ in range(4):
        boggle.append(list(input().strip()))
    print(*solve(boggle, words))
    try:
        input()
    except:
        pass
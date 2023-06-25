import sys

trie = {}
def add(trie, word):
    ptr = trie
    for i in word:
        if i not in ptr: ptr[i] = {}
        ptr = ptr[i]
        if '.' not in ptr: ptr['.'] = 0
        ptr['.'] += 1

input()
for w in sys.stdin:
    w = w.strip()
    add(trie, w)
    ptr = trie
    for i in w: ptr = ptr[i]
    print(ptr['.']-1)
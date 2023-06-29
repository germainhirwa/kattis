# https://github.com/stevenhalim/cpbook-code/blob/master/ch6/sa_lcp.py
def sort_cyclic_shifts(s):
    s = [*map(ord, s)]
    n = len(s)
    alphabet = 256
    p = [0] * n
    c = [0] * n
    cnt = [0] * max(alphabet, n)
    for i in range(n):
        cnt[s[i]] += 1
    for i in range(1, alphabet):
        cnt[i] += cnt[i-1]
    for i in range(n):
        cnt[s[i]] -= 1
        p[cnt[s[i]]] = i
    c[p[0]] = 0
    classes = 1
    for i in range(1, n):
        if s[p[i]] != s[p[i-1]]:
            classes += 1
        c[p[i]] = classes - 1
    pn = [0] * n
    cn = [0] * n
    h = 0
    while (1 << h) < n:
        for i in range(n):
            pn[i] = p[i] - (1 << h)
            if pn[i] < 0:
                pn[i] += n
        for i in range(classes):
            cnt[i] = 0
        for i in range(n):
            cnt[c[pn[i]]] += 1
        for i in range(1, classes):
            cnt[i] += cnt[i-1]
        for i in range(n-1, -1, -1):
            cnt[c[pn[i]]] -= 1
            p[cnt[c[pn[i]]]] = pn[i]
        cn[p[0]] = 0
        classes = 1
        for i in range(1, n):
            cur = (c[p[i]], c[(p[i] + (1 << h)) % n])
            prev = (c[p[i-1]], c[(p[i-1] + (1 << h)) % n])
            if cur != prev:
                classes += 1
            cn[p[i]] = classes - 1
        c, cn = cn, c
        h += 1
    return p

def suffix_array_construction(s):
    return sort_cyclic_shifts(s+'\0')[1:]

def lcp_construction(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    k = 0
    lcp = [0] * (n-1)
    for i in range(n):
        if rank[i] == n-1:
            k = 0
            continue
        j = sa[rank[i]+1]
        while i + k < n and j + k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k:
            k -= 1
    return [0] + lcp

def longest_repeated_substring(lcp):
    idx = 0
    max_lcp = -1
    for i in range(1, len(lcp)):
        if lcp[i] > max_lcp:
            max_lcp = lcp[i]
            idx = i
    return (max_lcp, idx)

input()
s = input().strip()
print(longest_repeated_substring(lcp_construction(s, suffix_array_construction(s)))[0])
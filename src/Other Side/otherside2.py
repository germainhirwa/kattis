w, s, c, k = map(int, input().split())
print(['NO', 'YES'][int(s < k or w + c < k or (s == k and w + c <= 2*k) or (w + c == k and s <= 2*k))])
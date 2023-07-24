s, c, k = map(int, input().split())
w = 0; d = sorted(map(int, input().split()))
pos = 0; m = d[0]; l = 0
while pos < s:
    if abs(m-d[pos]) > k or l == c: w += 1; m = d[pos]; l = 0
    m = min(m, d[pos]); l += 1; pos += 1
print(w+1)
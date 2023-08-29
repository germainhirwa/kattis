s = input().strip()
ptr = 0; ans = []
m = {'R': 'S', 'B': 'K', 'L': 'H'}
cb = {'RBL', 'RLB', 'LRB', 'LBR', 'BRL', 'BLR'}
while ptr < len(s):
    if s[ptr:ptr+3] in cb: ptr += 3; ans.append('C')
    else: ans.append(m[s[ptr]]); ptr += 1
print(''.join(ans))
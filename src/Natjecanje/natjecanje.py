n, s, r = map(int, input().split())
td = {*map(int, input().split())}
tr = {*map(int, input().split())}
td, tr = td-tr, tr-td

def opt(td, tr):
    if not tr or not td: return len(td)
    ans = len(td)
    for i in tr:
        tr2 = tr.copy() - {i}
        for j in [i-1, i+1]:
            if j in td: ans = min(ans, opt(td.copy() - {j}, tr2))
    return ans

print(opt(td, tr))
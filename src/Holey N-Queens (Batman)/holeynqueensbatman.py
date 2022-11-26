import sys

def nqueen(n, holes):
    def backtrack(assgn, dom, adds, subs):
        if len(assgn) == n: return 1
        sol, r = 0, len(assgn)
        for c in range(n):
            s = r - c + n - 1
            if dom[c] and r*n+c not in holes and not adds[r + c] and not subs[s]:
                assgn.append(r*n+c)
                dom[c] -= 1
                adds[r + c] += 1
                subs[s] += 1
                sol += backtrack(assgn, dom, adds, subs)
                subs[s] -= 1
                adds[r + c] -= 1
                dom[c] += 1
                assgn.pop()
        return sol
    return backtrack([], [1]*n, [0]*(2*n), [0]*(2*n))

while True:
    n, m = map(int, input().split())
    if n + m == 0: break
    holes = set()
    if m > 0:
        for line in sys.stdin:
            m -= 1
            r, c = map(int, line.split())
            holes.add(r*n+c)
            if m == 0: break
    print(nqueen(n, holes))
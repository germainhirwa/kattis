import sys
input()

def check_back(exp, assgn, carry):
    try:
        d = carry
        for i in exp[:-1]:
            if i:
                d += assgn[i[-1]]
        e = assgn[exp[-1][-1]]
        return (d % 10 == e % 10, d//10)
    except:
        return False

letters = set()
exp = []
domains = set(range(10))
mem = set()

for line in sys.stdin:
    exp.append(list(line.strip()))
    letters |= set(line.strip())
leads = {i[0] for i in exp}

def backtrack(exp, domains, assgn, carry=0):
    for i in leads: # leading digit cannot be 0
        if i in assgn and assgn[i] == 0:
            return
    if not any(exp) and carry == 0:
        mem.add(tuple(sorted(assgn.items())))
        return
    t = check_back(exp, assgn, carry)
    if not (type(t) == tuple and not t[0]):
        # t = False or t = (True, ...)
        if t != False:
            exp = list(map(lambda x: x[:-1], exp))
            carry = t[1]
            if not any(exp[:-1]) and exp[-1] and carry:
                if exp[-1][-1] in assgn and assgn[exp[-1][-1]] == carry:
                    mem.add(tuple(sorted(assgn.items())))
                    return
                if exp[-1][-1] not in assgn and carry in domains:
                    mem.add(tuple(sorted(list(assgn.items()) + [(exp[-1][-1], carry)])))
                    return
        if not any(exp) and not carry:
            mem.add(tuple(sorted(assgn.items())))
            return
        rec = False
        for i in {i[-1] for i in exp if i}:
            if i not in assgn:
                rec = True
                for domain in sorted(domains):
                    assgn[i] = domain # pick a domain
                    domains -= {assgn[i]} # update domains
                    backtrack(exp, domains, assgn, carry)
                    domains.add(assgn[i]) # revert domains
                    del assgn[i] # revert assgn
                break
        if t != False and not rec:
            backtrack(exp, domains, assgn, carry)
    return

backtrack(exp, domains, {})
print(len(mem))
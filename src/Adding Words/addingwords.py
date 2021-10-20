import sys
vars = {}
rev_vars = {}

for line in sys.stdin:
    k = line.strip().split()
    if k[0] == "def":
        if k[1] not in vars:
            vars[k[1]] = int(k[2])
            rev_vars[int(k[2])] = k[1]
        else:
            rev_vars.pop(vars[k[1]])
            rev_vars[int(k[2])] = k[1]
            vars[k[1]] = int(k[2])
    elif k[0] == "calc":
        s = 0
        plus = True
        known = True
        for op in k[1:]:
            if op == "+":
                plus = True
            elif op == "-":
                plus = False
            elif op != "=": # variable
                if op in vars:
                    if plus:
                        s += vars[op]
                    else:
                        s -= vars[op]
                else:
                    known = False
                    break
        
        if known and s in rev_vars:
            print(" ".join(k[1:]) + " " + rev_vars[s])
        else:
            print(" ".join(k[1:]) + " unknown")
    else: # clear
        vars.clear()
        rev_vars.clear()
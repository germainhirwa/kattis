import sys

d, cd, n = True, True, True

for line in sys.stdin:
    if d:
        d = False
    elif cd:
        cd = False
        cdm = line.strip().split()[1:]
    elif n:
        n = False
        nn = int(line)
        lr, rl = {}, {}
    else:
        a, b = line.strip().split(" -> ")
        lr[a] = lr.get(a, []) + [b]
        rl[b] = rl.get(b, []) + [a]
        nn -= 1

        if nn == 0:
            d, cd, n = True, True, True
            def do():
                injective, surjective = True, True
                for k in lr:
                    if len(lr[k]) > 1:
                        return "not a function"
                
                for k in cdm:
                    if len(rl.get(k, [])) > 1:
                        injective = False
                    elif len(rl.get(k, [])) == 0:
                        surjective = False

                if surjective and injective:
                    return "bijective"
                elif surjective:
                    return "surjective"
                elif injective:
                    return "injective"
                return "neither injective nor surjective"
            
            print(do())
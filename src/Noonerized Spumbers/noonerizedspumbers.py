a, op, b, eq, c = input().strip().split()
can = False
import sys
for i in range(len(a)):
    for j in range(len(b)):
        if not can:
            exp = f'{b[:j]+a[i:]} {op} {a[:i]+b[j:]} == {c}'
            try:
                if eval(exp): print(exp.replace('==', '=')); can = True
            except: pass
for i in range(len(b)):
    for j in range(len(c)):
        if not can:
            exp = f'{a} {op} {c[:j]+b[i:]} == {b[:i]+c[j:]}'
            try:
                if eval(exp): print(exp.replace('==', '=')); can = True
            except: pass
for i in range(len(a)):
    for j in range(len(c)):
        if not can:
            exp = f'{c[:j]+a[i:]} {op} {b} == {a[:i]+c[j:]}'
            try:
                if eval(exp): print(exp.replace('==', '=')); can = True
            except: pass
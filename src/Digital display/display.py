import sys

d = {0: '''
+---+
|   |
|   |
+   +
|   |
|   |
+---+
''', 1: '''
    +
    |
    |
    +
    |
    |
    +
''', 2: '''
+---+
    |
    |
+---+
|    
|    
+---+
''', 3: '''
+---+
    |
    |
+---+
    |
    |
+---+
''', 4: '''
+   +
|   |
|   |
+---+
    |
    |
    +
''', 5: '''
+---+
|    
|    
+---+
    |
    |
+---+
''', 6: '''
+---+
|    
|    
+---+
|   |
|   |
+---+
''', 7: '''
+---+
    |
    |
    +
    |
    |
    +
''', 8: '''
+---+
|   |
|   |
+---+
|   |
|   |
+---+
''', 9: '''
+---+
|   |
|   |
+---+
    |
    |
+---+
'''
}

for line in sys.stdin:
    line = line.strip()
    if line != 'end':
        h, m = line.split(':')
        (h1, h2), (m1, m2) = h, m
        clock = [[' ']*29 for _ in range(7)]
        clock[2][14] = clock[4][14] = 'o'
        for i, o in ((h1, 0), (h2, 7), (m1, 17), (m2, 24)):
            for e, p in enumerate(d[int(i)][1:-1].split('\n')):
                for e2, q in enumerate(p):
                    clock[e][o+e2] = q
        for r in clock: print(''.join(r))
        print();print()
    else: print(line)
while True:
    n = int(input())
    if n == 0:
        break
    
    boxes = []
    for _ in range(n):
        x1, y1, x2, y2, sz = input().split()
        boxes.append((float(x1), float(y1), float(x2), float(y2), sz))
    
    for _ in range(int(input())):
        x, y, sz = input().split()
        x, y = float(x), float(y)
        found = False
        for box in boxes:
            x1, y1, x2, y2, sz2 = box
            if x1 <= x <= x2 and y1 <= y <= y2:
                found = True
                if sz == sz2:
                    print(sz, 'correct')
                else:
                    print(sz, sz2)
                break
        if not found:
            print(sz, 'floor')
    print()
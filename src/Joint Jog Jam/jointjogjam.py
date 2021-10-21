nums = list(map(int, input().split()))
d = 0
for px, py, qx, qy in [nums[:4], nums[4:]]:
    d = max(d, ((px - qx)**2 + (py - qy)**2)**0.5)
print(d)
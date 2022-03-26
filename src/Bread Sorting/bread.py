def inv_idx(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += inv_idx(arr, left, mid) + inv_idx(arr, mid + 1, right)
        inv_count += merge(arr, left, mid, right)
    return inv_count

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    inv_count = 0
    temp = []

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inv_count += (mid - i + 1)
            j += 1

    temp.extend(arr[i:mid+1])
    temp.extend(arr[j:right+1])

    for idx in range(left, right + 1):
        arr[idx] = temp[idx - left]

    return inv_count

n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
d = {}
for i in range(n):
    d[b[i]] =  i

print(['Possible', 'Impossible'][inv_idx(list(map(lambda x: d[x], a)), 0, n - 1) % 2])
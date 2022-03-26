n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

freq1, freq2 = {}, {}
for i in range(n):
    if arr1[i] not in freq1:
        freq1[arr1[i]] = 0
    freq1[arr1[i]] += 1
    if arr2[i] not in freq2:
        freq2[arr2[i]] = 0
    freq2[arr2[i]] += 1

    print(arr2[i], end=' ')
    if freq1 == freq2 and i != n - 1:
        freq1.clear()
        freq2.clear()
        print('#', end=' ')
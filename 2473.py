n = int(input())
arr = sorted(list(map(int, input().split())))
min = 1000000000000000000000
index = []
for first in arr:
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        if first == arr[p1]:
            p1 += 1
            continue
        if first == arr[p2]:
            p2 -= 1
            continue
        temp = first + arr[p1] + arr[p2]
        if abs(temp) < abs(min):
            min = temp
            index = sorted([first, arr[p1], arr[p2]])
        if temp < 0:
            p1 += 1
        else:
            p2 -= 1
print(*index)

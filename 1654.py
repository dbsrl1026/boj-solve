import math


def binarySearch(start, end, arr, N):
    temp = math.floor((start + end) / 2)
    if temp == start:
        return temp
    sum = 0
    for j, v in enumerate(arr):
        sum += math.floor(v / temp)
    if sum >= N:
        return binarySearch(temp, end, arr, N)
    else:
        return binarySearch(start, temp, arr, N)


K, N = map(int, input().split())
arr = []
for i in range(K):
    arr.append(int(input()))
result = binarySearch(0, max(arr)+1, arr, N)
print(result)
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
min = 10000000000
answer = []
for first in arr:
    start = 0
    end = n-1
    while start < end:
        if first == arr[start]:
            start += 1
            continue
        if first == arr[end]:
            end -= 1
            continue
        summ = first + arr[start] + arr[end]
        if abs(summ) < abs(min):
            min = summ
            answer = [first, arr[start], arr[end]]
        if summ < 0:
            start += 1
        else:
            end -= 1
print(*answer)

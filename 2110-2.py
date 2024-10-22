n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
start = 0
end = arr[-1] - arr[0] + 1

while start < end:
    mid = int((start+end)/2)
    temp = arr[0]
    remain_c = c - 1
    low_flag = False
    high_flag = False
    for i in range(1,n):
        if arr[i] - temp >= mid:
            temp = arr[i]
            remain_c -= 1
            if remain_c <= 0:
                low_flag = True
                break
    if remain_c > 0:
        high_flag = True
    if low_flag:
        start = mid + 1
    elif high_flag:
        end = mid

print(start-1)
n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
diff = []
for i in range(1, n):
    diff.append(arr[i] - arr[i - 1])
start = 0
end = arr[-1] - arr[0]
while start <= end:
    mid = int((start + end) / 2)
    temp = 0
    tc = c-1
    for k, v in enumerate(diff):
        temp += v
        if temp >= mid:
            temp = 0
            tc -= 1
        if tc == 0:
            if start == end:
                print(start)
                exit()
            start = mid + 1
            break
    if tc > 0:
        if start == end:
            print(start - 1)
            exit()
        end = mid

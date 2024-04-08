n = int(input())
k = int(input())

start = 1
end = n**2
answer = 0
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(1, n + 1):
        temp += min(mid // i, n)

    if temp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)

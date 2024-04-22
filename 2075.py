import heapq
n = int(input())
arr = []
heap = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    if i == n-1:
        for j in range(n):
            heapq.heappush(heap,(-arr[i][j],i,j))
for _ in range(n):
    answer,i,j = heapq.heappop(heap)
    heapq.heappush(heap,(-arr[i-1][j],i-1,j))
print(-answer)



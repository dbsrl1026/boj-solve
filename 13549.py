import heapq

n,k = map(int,input().split())
if n>k:
    print(n-k)
    exit()
queue = []
visited = []
heapq.heappush(queue,(0,n))

while queue:
    cnt, temp =heapq.heappop(queue)
    if temp == k:
        break
    if temp in visited or temp<0 or temp>100000:
        continue
    visited.append(temp)
    heapq.heappush(queue, (cnt, temp*2))
    heapq.heappush(queue, (cnt+1, temp-1))
    heapq.heappush(queue, (cnt+1, temp+1))
print(cnt)
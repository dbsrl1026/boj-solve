from collections import deque

n,k = map(int,input().split())
if n>k:
    print(n-k)
    exit()
queue = deque()
visited = []
queue.append((n,0))

while queue:
    temp, cnt =queue.popleft()
    if temp == k:
        break
    if temp in visited or temp<0 or temp>100000:
        continue
    visited.append(temp)
    queue.append((temp-1,cnt+1))
    queue.append((temp + 1, cnt + 1))
    queue.append((temp *2, cnt + 1))
print(cnt)
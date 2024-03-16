from collections import deque

n,k = map(int,input().split())
queue = deque()
visited = {n:0}
queue.append((n,0))
arrive = 0
minn = 0
end =False
dt = [-1,1]
while queue:
    temp, cnt = queue.popleft()
    if end == True:
        if cnt > minn:
            break
        elif cnt == minn and temp == k:
            arrive += 1
        else:
            continue
    else:
        if temp == k:
            end = True
            minn = cnt
            arrive += 1
            continue
        for i in range(2):
            next = temp + dt[i]
            if (next not in visited or visited[next] == cnt+1) and 0 <= next <= 100000:
                queue.append((next, cnt+1))
                visited[next] = cnt+1
        next = temp *2
        if (next not in visited or visited[next] == cnt+1) and 0 <= next <= 100000:
            queue.append((next, cnt + 1))
            visited[next] = cnt+1
print(minn)
print(arrive)
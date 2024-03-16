from collections import deque

v, e = map(int, input().split())
graph = {}
visited = {}
for i in range(1,v+1):
    graph[i] = []
for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
cnt = 0
for i in range(1,v+1):
    if i in visited:
        continue
    cnt +=1
    queue = deque()
    visited[i] = True
    queue.append(i)
    while queue:
        temp = queue.popleft()
        for _,v in enumerate(graph[temp]):
            if v not in visited:
                queue.append(v)
                visited[v] = True
print(cnt)
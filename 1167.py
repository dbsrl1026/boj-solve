
from collections import deque

n = int(input())
graph = {}
length = {}

for i in range(n):
    temp = list(map(int, input().split()))
    name = temp.pop(0)
    graph[name] = []
    for j in range(0, len(temp), 2):
        if temp[j] == -1:
            break
        graph[name].append(temp[j])
        length[(name, temp[j])] = temp[j + 1]
visited = {1: 0}
queue = deque()
queue.append((1, 0))
while queue:
    temp, leng = queue.popleft()
    for _, v in enumerate(graph[temp]):
        if v not in visited:
            newLeng = leng + length[(temp, v)]
            queue.append((v, newLeng))
            visited[v] = newLeng
visited = sorted(visited.items(),key=lambda x:x[1], reverse=True)
start = visited[0][0]
visited = {start:True}
queue = deque()
queue.append((start, 0))
maxx = 0
while queue:
    temp, leng = queue.popleft()
    maxx = max(maxx, leng)
    for _, v in enumerate(graph[temp]):
        if v not in visited:
            newLeng = leng + length[(temp, v)]
            queue.append((v, newLeng))
            visited[v] =True
print(maxx)

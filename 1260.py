from collections import deque


def dfs(dic,v,visited):
    visited.append(v)
    dic[v] = sorted(dic[v])
    for i,e in enumerate(dic[v]):
        if e not in visited:
            visited = dfs(dic,e,visited)
    return visited

def bfs(dic,v):
    visited = []
    queue = deque()
    queue.append(v)
    while queue:
        cur = queue.popleft()
        if cur in visited:
            continue
        visited.append(cur)
        dic[cur] = sorted(dic[cur])
        queue.extend(dic[cur])

    return visited

p,l,v = map(int,input().split())
dic ={}
for i in range(1,p+1):
    dic[i] = []
for i in range(l):
    x,y = map(int,input().split())
    dic[x].append(y)
    dic[y].append(x)
print(*dfs(dic,v,[]))
print(*bfs(dic,v))
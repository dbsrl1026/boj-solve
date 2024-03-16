def dfs(graph, visited, v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())  # 약들의 관계
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
dfs(graph, visited, 0)
if all(visited):
    print(1)
else:
    print(0)


lab2

from collections import defaultdict

def dfs(graph, node, visited):
    visited[node] = True
    max_distance = 0

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            distance = dfs(graph, neighbor, visited) + weight
            if distance > max_distance:
                max_distance = distance

    return max_distance

def diameter(graph):
    n = len(graph)
    d = 0

    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        distance = dfs(graph, i, visited)
        if distance > d:
            d = distance

    return d

n = int(input())  # 건물 수
graph = defaultdict(list)

for _ in range(n - 1):
    a, b, weight = map(int, input().split())  # 건물 간 연결 및 가중치
    graph[a].append((b, weight))
    graph[b].append((a, weight))

result = diameter(graph)
print(result)
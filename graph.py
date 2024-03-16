from collections import deque

graph = {
    1:[3,5],
    2:[4,5],
    3:[1,5],
    4:[2,5],
    5:[1,2,3,4]
}

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v =queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

def dfs(graph, cur_v, visited=[]):
    visited.append[cur_v]
    for v in graph[cur_v]:
        if v not in visited:
            dfs(graph,v,visited)
    return visited
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
map_graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
answer = deepcopy(map_graph)
same_zero_area = [0, 0]
num = 2
for i in range(n):
    for j in range(m):
        if map_graph[i][j] == 0:
            map_graph[i][j] = num
            same_zero_area.append(1)
            visit = deque()
            visit.append((i, j,))
            while visit:
                x, y = visit.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or map_graph[nx][ny] != 0:
                        continue
                    map_graph[nx][ny] = num
                    same_zero_area[num] += 1
                    visit.append((nx, ny,))
            num += 1
for i in range(n):
    for j in range(m):
        if map_graph[i][j] != 1:
            continue
        count = 1
        check = {}
        for dir in range(4):
            nx = i + dx[dir]
            ny = j + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if check.get(map_graph[nx][ny], 0):
                continue
            check[map_graph[nx][ny]] = 1
            count += same_zero_area[map_graph[nx][ny]]
        answer[i][j] = count % 10
for i in answer:
    print("".join(list(map(str, i))))

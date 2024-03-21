from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def bfs(visited):
    global ans

    queue = deque([[0, 0]])
    visited[0][0] = True
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nc < 0 or nc >= w + 2 or nr < 0 or nr >= h + 2 or grid[nr][nc] == '*' or visited[nr][nc]:
                continue

            if 'A' <= grid[nr][nc] <= 'Z':
                if chr(ord(grid[nr][nc]) + 32) not in key:
                    continue # 컨티뉴
            elif 'a' <= grid[nr][nc] <= 'z':
                if grid[nr][nc] not in key:
                    key[grid[nr][nc]] = True
                    visited = [[False] * (w + 2) for _ in range(h + 2)]
            elif grid[nr][nc] == "$" and (nr, nc) not in visited_doc:
                ans += 1
                visited_doc.append((nr, nc))

            visited[nr][nc] = True
            queue.append([nr, nc])

T = int(input())

for _ in range(1, T + 1):
    h, w = map(int, input().split())

    grid = ['.' + input() + '.' for _ in range(h)]
    grid = ['.' * (w + 2)] + grid + ['.' * (w + 2)]
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    key = {}
    visited_doc = []

    for i in input():
        if i.isalpha():
            key[i] = True 
    ans = 0
    bfs(visited)
    print(ans)
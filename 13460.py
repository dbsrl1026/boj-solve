from collections import deque

n, m = map(int, input().split())
grid = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    grid[i] = list(map(str, input()))
cur_R = 0
cur_B = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'R':
            grid[i][j] = '.'
            cur_R = (i, j)
        if grid[i][j] == 'B':
            grid[i][j] = '.'
            cur_B = (i, j)


def moving(cur_R, cur_B, dir):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    while dir < 4:
        Rx, Ry = cur_R
        Bx, By = cur_B
        if cur_R == (0, 0):
            next_R = cur_R
        elif grid[Rx + dx[dir]][Ry + dy[dir]] == '.' and cur_B != (Rx + dx[dir],Ry + dy[dir]):
            next_R = (Rx + dx[dir], Ry + dy[dir])
        elif grid[Rx + dx[dir]][Ry + dy[dir]] == 'O':
            next_R = (0, 0)
        else:
            next_R = cur_R

        if cur_B == (0, 0):
            next_B = cur_B
        if grid[Bx + dx[dir]][By + dy[dir]] == '.' and cur_R != (Bx + dx[dir],By + dy[dir]):
            next_B = (Bx + dx[dir], By + dy[dir])
        elif grid[Bx + dx[dir]][By + dy[dir]] == 'O':
            next_B = (0, 0)
        else:
            next_B = cur_B

        if cur_R == next_R and cur_B == next_B:
            break;
        else:
            cur_R = next_R
            cur_B = next_B
    if cur_R == (0, 0) and cur_B != (0, 0):
        return cur_R, cur_B, 1
    else:
        return cur_R, cur_B, 0


queue = deque()
queue.append((cur_R, cur_B, 4, 0))
while queue:
    R, B, dir, cnt = queue.popleft()
    R, B, result = moving(R, B, dir)
    if result == 1:
        print(cnt)
        exit(0)
    for i in range(4):
        if cnt < 10:
            queue.append((R, B, i, cnt + 1))
print(-1)

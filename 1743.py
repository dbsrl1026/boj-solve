import sys
sys.setrecursionlimit(10 ** 6)
n, m, k = map(int, input().split())
board = [[0] * (m + 1) for _ in range(n + 1)]
visit = [[0] * (m + 1) for _ in range(n + 1)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1


def search(x, y):
    cnt = 1
    visit[x][y] = 1
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if (mx <= 0 or my <= 0 or mx > n or my > m):
            continue
        if board[mx][my] > 0 and visit[mx][my] == 0:
            cnt += search(mx, my)
    return cnt


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if board[i][j] == 1 and visit[i][j] == 0:
            board[i][j] = search(i, j)

print(max(map(max, board)))

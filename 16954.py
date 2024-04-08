import sys

sys.setrecursionlimit(10 ** 9)
grid = []
for _ in range(8):
    grid.append(list(input()))
dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, 0, -1, -1, -1]


def dfs(board, nowX, nowY):
    if nowX == 0 and nowY == 7:
        return True
    for i in range(9):
        newX = nowX + dx[i]
        newY = nowY + dy[i]
        if 0 <= newX < 8 and 0 <= newY < 8 and board[newX][newY] != '#' and (newX == 0 or board[newX - 1][newY] != '#'):
            if dfs([['.', '.', '.', '.', '.', '.', '.', '.']] + board[:7], newX, newY):
                return True
    return False


if dfs(grid, 7, 0):
    print(1)
else:
    print(0)

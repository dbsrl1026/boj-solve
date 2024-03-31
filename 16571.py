grid = []
for _ in range(3):
    grid.append(list(map(int, input().split())))

xnum = 0
onum = 0
for i in range(3):
    for j in range(3):
        if grid[i][j] == 1:
            xnum += 1
        elif grid[i][j] == 2:
            onum += 1
if xnum == onum:
    player = 1
else:
    player = 2


def isEnd(game):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == 1 \
                or game[0][i] == game[1][i] == game[2][i] == 1:
            return 1
    if game[0][0] == game[1][1] == game[2][2] == 1 \
            or game[2][0] == game[1][1] == game[0][2] == 1:
        return 1

    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == 2 \
                or game[0][i] == game[1][i] == game[2][i] == 2:
            return 2
    if game[0][0] == game[1][1] == game[2][2] == 2 \
            or game[2][0] == game[1][1] == game[0][2] == 2:
        return 2

    empty = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                empty += 1
    if empty == 0:
        return 0
    return False


def dfs(game, turn):
    if turn == 3:
        turn = 1
    end = isEnd(game)
    if end:
        if end == 0:
            return 0
        elif end != turn:
            return -1
    best = 2
    for i in range(3):
        for j in range(3):
            if game[i][j] == 0:
                game[i][j] = turn
                best = min(best,dfs(game, turn + 1))
                game[i][j] = 0
    if best == 1:
        return -1
    elif best == 0 or best == 2:
        return 0
    else:
        return 1

ans = dfs(grid, player)
if ans == 1:
    print('W')
elif ans == 0:
    print('D')
else:
    print('L')
mask1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]


def check(startY, startX, board):
    result1 = 0
    result2 = 0
    for i in range(8):
        for j in range(8):
            if board[startY + i][startX + j] == mask1[i][j]:
                result1 += 1
            else:
                result2 += 1
    return min(result1, result2)


N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(input()))

Min = 64
for i in range(N - 7):
    for j in range(M - 7):
        result = check(i, j, board)
        Min = min(Min, result)
print(Min)

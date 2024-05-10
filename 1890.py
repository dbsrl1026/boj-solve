n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ch_board = [[0] * n for _ in range(n)]

ch_board[0][0] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] != 0 and ch_board[i][j] != 0:
            if i + board[i][j] < n:
                ch_board[i + board[i][j]][j] += ch_board[i][j]
            if j + board[i][j] < n:
                ch_board[i][j + board[i][j]] += ch_board[i][j]
print(ch_board[-1][-1])

n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))


def check(plus, minus, x, y):
    if grid[x][y] == 0:
        return False
    if x + y in plus:
        return False
    if x - y in minus:
        return False
    return True

def dfs(plus, minus, x, y):
    best = 0
    i = x
    j = y
    while i < n:
        if check(plus, minus, i, j):
            plus[i + j] = True
            minus[i - j] = True
            best = max(best, dfs(plus, minus, i, j) + 1)
            del plus[i + j]
            del minus[i - j]
        j += 2
        if j >= n:
            i += 1
            if n % 2 == 0:
                j = (j - n + 1) % 2
            else:
                j -= n
    return best

if n == 1:
    print(dfs({}, {}, 0, 0))
else:
    print(dfs({}, {}, 0, 0) + dfs({}, {}, 0, 1))

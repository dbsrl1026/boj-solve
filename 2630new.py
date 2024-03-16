n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

def dnc(piece , m):
    if len(set(piece)) > 1:
        mid = m // 2
        top_left = [row[:mid] for row in piece[:mid]]
        top_right = [row[mid:] for row in piece[:mid]]
        bottom_left = [row[:mid] for row in piece[mid:]]
        bottom_right = [row[mid:] for row in piece[mid:]]
        sump = dnc(top_left, mid) +dnc(top_right, mid)+dnc(bottom_left, mid)+dnc(bottom_right, mid)
        return sump
    else:
        return 1
print(dnc(grid, n))
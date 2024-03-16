import sys

n = int(sys.stdin.readline())
point = set()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(n):
    x, y, d, g = map(int, sys.stdin.readline().split())
    point.add((x, y))
    directions = [d]
    for _ in range(g):
        for i in reversed(directions):
            directions += [(i+1)%4]
    for dd in directions:
        x += dx[dd]
        y += dy[dd]
        point.add((x,y))
square = 0
for x, y in point:
    if (x+1, y) in point and (x, y+1) in point and (x+1, y+1) in point:
        square += 1

print(square)
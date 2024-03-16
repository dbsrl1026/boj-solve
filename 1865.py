import sys


def bellmanFord(edge, v):
    INF = int(100000000)
    dist = [INF] * (v + 1)
    dist[1] = 0
    for i in range(v):
        for start, end, time in edge:
            if  dist[end] > dist[start] + time:
                if i == v - 1:
                    return 'YES'
                dist[end] = dist[start] + time
    return 'NO'


tc = int(sys.stdin.readline())
for _ in range(tc):
    v, e, w = map(int, sys.stdin.readline().split())
    edge = []
    for _ in range(e):
        start, end, time = map(int, sys.stdin.readline().split())
        edge.append((start, end, time))
        edge.append((end, start, time))
    for _ in range(w):
        start, end, time = map(int, sys.stdin.readline().split())
        edge.append((start, end, -time))
    print(bellmanFord(edge, v))


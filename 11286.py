import heapq
import sys

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    c = int(sys.stdin.readline())
    if c != 0:
        heapq.heappush(heap,(abs(c),c))
    elif heap:
        print(heapq.heappop(heap)[1])
    else:
        print(0)
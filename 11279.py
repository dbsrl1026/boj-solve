import heapq
import sys

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    i = int(sys.stdin.readline())
    if i != 0:
        heapq.heappush(heap,(-i,i))
    elif heap :
        print(heapq.heappop(heap)[1])
    else:
        print(0)
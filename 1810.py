import heapq
import math
import sys

input = sys.stdin.readline
n, f = map(int, input().split())
stones = {}
heap = []
costs = {}
for i in range(n):
    stones[tuple(map(int, input().split()))] = True
heapq.heappush(heap, (0, 0, 0))

while heap:
    cur_cost, cur_x, cur_y = heapq.heappop(heap)
    if cur_y == f:
        print(round(cur_cost))
        exit(0)
    if (cur_x, cur_y) not in costs:
        costs[(cur_x, cur_y)] = cur_cost
        for next_x in range(cur_x-2, cur_x+3):
            for next_y in range(cur_y-2,cur_y+3):
                if (next_x,next_y) in stones:
                    next_cost = cur_cost + math.sqrt((cur_x - next_x) ** 2 + (cur_y - next_y) ** 2)
                    heapq.heappush(heap, (next_cost, next_x, next_y))
print(-1)

import sys
import heapq
input = sys.stdin.readline

n = int(input())
under = []
under_max = -float('inf')
over = []
over_min = float('inf')
for _ in range(n):
    temp = int(input())
    if len(under) == len(over):
        if temp <= over_min:
            heapq.heappush(under,-temp)
            under_max = max(under_max,temp)
        else:
            heapq.heappush(over,temp)
            heapq.heappop(over)
            heapq.heappush(under, -over_min)
            under_max = over_min
            over_min =  heapq.heappop(over)
            heapq.heappush(over, over_min)
    elif len(under) > len(over):
        if temp < under_max:
            heapq.heappush(under,-temp)
            heapq.heappop(under)
            heapq.heappush(over,under_max)
            over_min = under_max
            under_max = -heapq.heappop(under)
            heapq.heappush(under, -under_max)
        else:
            heapq.heappush(over,temp)
            over_min = min(over_min,temp)
    print(under_max)

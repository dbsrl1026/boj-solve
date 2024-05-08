import sys
input = sys.stdin.readline
import heapq
n, k = map(int, input().split())
jewels = []
for i in range(n):
    heapq.heappush(jewels, tuple(map(int, input().split())))
knapsacks = []
for i in range(k):
    knapsacks.append(int(input()))
knapsacks = sorted(knapsacks)

result = 0
temp = []

for knap in knapsacks:
    while jewels and jewels[0][0] <= knap:
        heapq.heappush(temp, -jewels[0][1])
        heapq.heappop(jewels)
    if temp:
        result -= heapq.heappop(temp)
print(result)
import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq
n, m = map(int, input().split())
dict = defaultdict(list)
pretends = [0] * (n+1)
heap = []
result = []
for i in range(m):
    a,b = map(int,input().split())
    dict[a].append(b)
    pretends[b] += 1

for i in range(1, n+1):
    if pretends[i] == 0:
        heapq.heappush(heap,i)

while heap:
    temp = heapq.heappop(heap)
    result.append(temp)
    for next in dict[temp]:
        pretends[next] -= 1
        if pretends[next] == 0:
            heapq.heappush(heap, next)

print(*result)
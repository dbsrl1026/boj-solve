#bfs
from collections import deque
import copy

n = int(input())
arr = list(map(int, input().split()))

maxx = 0
queue = deque()

queue.append((arr, 0))

while queue:
    temp, sum = queue.popleft()
    if len(temp) == 2:
        if sum > maxx:
            maxx = sum
    else:
        for i in range(2, len(temp)):
            temp2 = copy.deepcopy(temp)
            add = temp2[i] * temp2[i - 2]
            del temp2[i - 1]
            queue.append((temp2, sum + add))
print(maxx)
import sys
import heapq
num = int(sys.stdin.readline())
arr = []
s = ''
for i in range(num):
    dist = int(sys.stdin.readline())
    if dist == 0:
        if not arr:
            s += '0'+'\n'
        else:
            s += str(heapq.heappop(arr)) + '\n'
    else:
        heapq.heappush(arr, dist)
print(s)
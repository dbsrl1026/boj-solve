import copy
import heapq
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
heap = copy.deepcopy(arr)
heapq.heapify(heap)
dic = {}
cnt = 0
prev = False
for i in range(n):
    temp = heapq.heappop(heap)
    if temp != prev:
        dic[temp] = cnt
        cnt += 1
    prev = temp
answer = []
for i, v in enumerate(arr):
    answer.append(dic[v])
print(*answer)

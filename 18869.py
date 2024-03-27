import sys
from collections import defaultdict
m, n = map(int, sys.stdin.readline().split())

dict = defaultdict(int)
for i in range(m):
    planets = list(map(int, sys.stdin.readline().split()))
    sortedPlanets = sorted(list(set(planets)))
    rank = {sortedPlanets[i]: i for i in range(len(sortedPlanets))}
    vector = tuple([rank[i] for i in planets])
    dict[vector] += 1


cnt = 0
for i in dict.values():
    cnt += (i * (i - 1)) // 2
print(cnt)

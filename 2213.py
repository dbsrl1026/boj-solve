from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
n = int(input())
costs = [0]
costs += list(map(int, input().split()))
edges = defaultdict(list)
dp = {}
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(cur_node, prev_node, isInclude):
    if (cur_node, prev_node, isInclude) in dp:
        return dp[(cur_node, prev_node, isInclude)]
    cost_sum = 0
    vertexs = []
    if isInclude:
        vertexs.append(cur_node)
        cost_sum += costs[cur_node]
        for next_node in edges[cur_node]:
            if next_node == prev_node:
                continue
            temp = dfs(next_node,cur_node, False)
            cost_sum += temp[0]
            vertexs += temp[1]
    else:
        for next_node in edges[cur_node]:
            if next_node == prev_node:
                continue
            tempFalse = dfs(next_node,cur_node, False)
            tempTrue = dfs(next_node,cur_node, True)
            if tempFalse[0] > tempTrue[0]:
                cost_sum += tempFalse[0]
                vertexs += tempFalse[1]
            else:
                cost_sum += tempTrue[0]
                vertexs += tempTrue[1]
    dp[(cur_node, prev_node, isInclude)] = (cost_sum, vertexs)
    return (cost_sum, vertexs)


answer = max(dfs(1, 0, True), dfs(1, 0, False))

print(answer[0])
print(*sorted(answer[1]))

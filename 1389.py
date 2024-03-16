from collections import deque


def bfs(v, dic, visited, count):
    queue=deque()
    queue.append((v,count))
    while queue:
        cur, temp = queue.popleft()
        if cur in visited:
            continue
        visited.append(cur)
        count +=temp
        for i,e in enumerate(dic[cur]):
            queue.append((e,temp+1))
    return count


n, m = map(int,input().split())
dic={}
for i in range(1,n+1):
    dic[i] = []

for i in range(m):
    x, y = map(int,input().split())
    dic[x].append(y)
    dic[y].append(x)

bacon = []
for i in range(1,n+1):
    bacon.append(bfs(i,dic,[],0))

print(bacon.index(min(bacon))+1)
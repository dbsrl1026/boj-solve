from collections import deque

n = int(input())
own = list(map(int,input().split()))
m = int(input())
comp = []
temp = list(map(int,input().split()))
for i in range(m):
    comp.append([temp[i], i])

own = deque(sorted(own))
comp = deque(sorted(comp, key = lambda x: x[0]))
result = {}
for i in range(len(comp)):
    result[i] = 0


while comp:
    if not own:
        comp.popleft()
    else:
        if own[0] < comp[0][0]:
            own.popleft()
        elif own[0] == comp[0][0]:
            own.popleft()
            result[comp[0][1]]+=1
        else:
            comp.popleft()

    if len(comp)>1 and comp[0][0] == comp[1][0]:
        result[comp[1][1]] = result[comp[0][1]]

print(*result.values())



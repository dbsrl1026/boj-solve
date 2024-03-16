from collections import deque
v,e = map(int, input().split())
arr = []
for i in range(e):
    a,b,w = map(int, input().split())
    arr.append((w,a,b))
arr= deque(sorted(arr))
root = [i for i in range(v+1)]
weight_sum = 0

def findroot(x):
    if x != root[x]:
        root[x] = findroot(root[x])
    return root[x]


while arr:
    w, a, b = arr.popleft()
    aroot = findroot(a)
    broot = findroot(b)
    if aroot != broot:
        if aroot < broot:
            root[broot] = aroot
        else:
            root[aroot] = broot
        weight_sum += w

print(weight_sum)
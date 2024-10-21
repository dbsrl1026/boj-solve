import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
for i in range(n + 1):
    dict[i] = i

def find_parent(x):
    if dict[x] != x:
        dict[x] = find_parent(dict[x])
    return dict[x]

def union(a,b):
    root_a = find_parent(a)
    root_b = find_parent(b)
    if root_b != root_a:
        dict[root_b] = root_a

for _ in range(m):
    compute, a, b = map(int, input().split())
    if compute == 0:
        union(a,b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
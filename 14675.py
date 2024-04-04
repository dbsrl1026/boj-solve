from collections import defaultdict

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 2:
        print("yes")
    elif t == 1 and len(tree[k]) > 1:
        print("yes")
    else:
        print("no")

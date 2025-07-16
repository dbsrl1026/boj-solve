import sys
input = sys.stdin.readline

tree_size = 1
while tree_size < 2000001:
    tree_size *= 2
tree = [0] * (tree_size * 2)

def update(pos):
    pos += tree_size

    while pos > 0:
        tree[pos] += 1
        pos //= 2


def query_and_delete(b):
    pos = 1
    tree[pos] -= 1
    while pos < tree_size:
        pos *= 2
        temp = tree[pos]
        if b <= temp:
            tree[pos] -= 1
        else:
            b -= temp
            pos += 1
            tree[pos] -= 1
    return pos - tree_size



n = int(input())
for _ in range(n):
    a, b =  map(int, input().split())
    if a == 1:
        update(b)
    elif a == 2:
        print(query_and_delete(b))


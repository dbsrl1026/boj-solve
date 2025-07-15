import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

tree_size = 1
while tree_size < n:
    tree_size *= 2

tree = [0] * (tree_size * 2)
for i in range(n):
    tree[i + tree_size] = arr[i]
for i in range(tree_size - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]


def update(index, value):
    pos = tree_size + index
    tree[pos] = value
    while pos > 1:
        pos //= 2
        tree[pos] = tree[2 * pos] + tree[2 * pos + 1]


def query(left, right):
    left += tree_size
    right += tree_size
    res = 0
    while left <= right:
        if left % 2 == 1:
            res += tree[left]
            left += 1
        if right % 2 == 0:
            res += tree[right]
            right -= 1
        left //= 2
        right //= 2
    return res


for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b - 1, c)
    elif a == 2:
        print(query(b - 1, c - 1))

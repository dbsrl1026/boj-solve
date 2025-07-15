import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

tree_size = 1
while tree_size < n:
    tree_size *= 2

tree = [[1000000000,0] for _ in range(tree_size * 2)]
for i in range(n):
    tree[i + tree_size][0] = arr[i]
    tree[i + tree_size][1] = arr[i]
for i in range(tree_size - 1, 0, -1):
    tree[i][0] = min(tree[i * 2][0], tree[i * 2 + 1][0])
    tree[i][1] = max(tree[i * 2][1], tree[i * 2 + 1][1])


def query(left, right):
    left += tree_size
    right += tree_size
    q_min = 1000000000
    q_max = 0
    while left <= right:
        if left % 2 == 1:
            q_min = min(q_min, tree[left][0])
            q_max = max(q_max, tree[left][1])
            left += 1
        if right % 2 == 0:
            q_min = min(q_min, tree[right][0])
            q_max = max(q_max, tree[right][1])
            right -= 1
        left //= 2
        right //= 2
    return q_min, q_max


for _ in range(m):
    b, c = map(int, input().split())
    q_min, q_max = query(b-1, c-1)
    print(str(q_min) + " " + str(q_max))

n, k = map(int, input().split())

tree_size = 1

while tree_size < n:
    tree_size *= 2
tree = [0] * (tree_size * 2)

for i in range(n):
    tree[i + tree_size] = 1
for i in range(tree_size -1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

answer = []
prev = 0
remain = n
for i in range(n):
    curr = (prev + k) % remain
    if curr == 0:
        curr += remain
    prev = curr - 1
    pos = 1
    tree[pos] -= 1
    while pos < tree_size:
        pos *= 2
        temp = tree[pos]
        if curr <= temp:
            tree[pos] -= 1
        else:
            curr -= temp
            pos += 1
            tree[pos] -= 1
    answer.append(pos - tree_size + 1)
    remain -= 1
print('<' + ', '.join(map(str, answer)) + '>')

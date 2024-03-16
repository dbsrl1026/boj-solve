
n = int(input())
tree = []
for _ in range(n):
    tree.append(list(map(int, input().split())))
for i in range(n-2,-1,-1):
    for j in range(i+1):
        tree[i][j]+= max(tree[i+1][j],tree[i+1][j+1])
print(tree[0][0])

n, k = map(int, input().split())

thing=[[0,0]]
for i in range(n):
    thing.append(list(map(int, input())))
knap = [[0] * (k + 1) for _ in range(n + 1)]



for i in range(n):
    thing.append(list(map(int, input().split())))


for i in range(1, n+1):
    for j in range(1, k+1):
        weight = thing[i][0]
        value = thing[i][1]

        if j < weight:
            knap[i][j] = knap[i - 1][j]
        else:
            knap[i][j] = max(knap[i - 1][j], knap[i - 1][j - weight] + value)

print(knap[n][k])
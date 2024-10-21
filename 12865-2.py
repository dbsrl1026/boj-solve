num_of_things, volume = map(int, input().split())
thing = [[0, 0]]
for _ in range(num_of_things):
    thing.append(list(map(int, input().split())))

knapsack = [[0] * (volume + 1) for _ in range(num_of_things + 1)]

for i in range(1, num_of_things + 1):
    temp_weight = thing[i][0]
    temp_value = thing[i][1]
    for j in range(1, volume + 1):
        if j >= temp_weight:
            knapsack[i][j] = max(knapsack[i-1][j-temp_weight] + temp_value, knapsack[i-1][j])
        else:
            knapsack[i][j] = knapsack[i-1][j]

print(knapsack[num_of_things][volume])


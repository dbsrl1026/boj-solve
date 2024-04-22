n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))

sortedArr = sorted(arr)
answer = []

for i in range(n):
    answer.append(sortedArr[i][1] - arr[i][1])

print(max(answer) + 1)

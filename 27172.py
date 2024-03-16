n = int(input())
arr = list(map(int, input().split()))
dict = {}
for i in arr:
    dict[i] = True
dp = [0 for _ in range(1000001)]

for i in arr:
    mul = i * 2
    while mul <= 1000000:
        if mul in dict:
            dp[i] += 1
            dp[mul] -= 1
        mul += i
answer = []
for i in arr:
    answer.append(str(dp[i]))
print(' '.join(map(str,answer)))
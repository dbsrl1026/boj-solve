T = int(input())
testcase = []
for i in range(T):
    testcase.append(int(input()))

dp = [0 for _ in range(10)]
dp[9] = 1
answer = [0 for _ in range(max(testcase) + 1)]

for i in range(1, max(testcase) + 1):
    for j in range(10):
        dp[j] = sum(dp[j:])
    answer[i] = sum(dp)

for v in testcase:
    print(answer[v])

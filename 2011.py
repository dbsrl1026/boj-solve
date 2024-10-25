n = list(input())
if len(n) == 1:
    if n[0] == '0':
        print(0)
    else:
        print(1)
    exit(0)
dp = [0] * len(n)
if n[0] == '0' or (n[0] > '2' and n[1] == '0'):
    print(0)
    exit(0)
dp[0] = 1
if int(n[0] + n[1]) <= 26 and n[1] != '0':
    dp[1] = 2
else:
    dp[1] = 1

for i in range(2, len(n)):
    if n[i] != '0':
        dp[i] += dp[i - 1]
    if 10 <= int(n[i - 1] + n[i]) <= 26:
        dp[i] += dp[i - 2]
    if dp[i] == 0:
        print(0)
        exit(0)

print(dp[len(n) - 1] % 1000000)

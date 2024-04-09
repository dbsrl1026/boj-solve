s = list(input())
palindrome = [[False] * len(s) for _ in range(len(s))]
dp = [100000000000] * len(s)

for i in range(len(s)):
    palindrome[i][i] = True
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        palindrome[i][i + 1] = True

for i in range(3, len(s) + 1):
    for j in range(len(s) - i + 1):
        k = j + i - 1
        if s[j] == s[k] and palindrome[j + 1][k - 1]:
            palindrome[j][k] = True

for i in range(len(s)):
    if palindrome[0][i] == True:
        dp[i] = 1
    else:
        for j in range(i):
            if palindrome[j+1][i] and dp[j] + 1 < dp[i]:
                dp[i] = dp[j] + 1

print(dp[-1])

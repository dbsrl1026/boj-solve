str1 = " " + input()
str2 = " " + input()

dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
substr = [['' for _ in range(len(str2))] for _ in range(len(str1))]
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            substr[i][j] = substr[i - 1][j - 1] + str1[i]
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                substr[i][j] = substr[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
                substr[i][j] = substr[i][j - 1]

if dp[-1][-1] == 0:
    print(0)
else:
    print(dp[-1][-1])
    print(substr[-1][-1])
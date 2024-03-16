import math

n = int(input())

#dp = [0,1,2]

# for i in range(3, n+1):
#     if int(math.sqrt(i))**2 == i:
#         dp.append(1)
#     else:
#         minn = []
#         for j in range(1, int(i/2 + 1)):
#             minn.append(dp[j]+ dp[i-j])
#         dp.append(min(minn))
# print(dp[n])

dp = [x for x in range(n+1)]
for i in range(1, n+1):
    for j in range(1,int(math.sqrt(i))+1):
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1
print(dp[n])
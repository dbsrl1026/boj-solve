def climb(n):
    memo = {1 : 1, 2 : 2}
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]




n = int(input())
answer = climb(n)
print(answer)
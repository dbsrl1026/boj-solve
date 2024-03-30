n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
ans = []

def dfs(temp, index, pl, mi, mu, di):
    if index == n:
        ans.append(temp)
    else:
        if pl > 0:
            dfs(temp + nums[index], index + 1, pl - 1, mi, mu, di)
        if mi > 0:
            dfs(temp - nums[index], index + 1, pl, mi - 1, mu, di)
        if mu > 0:
            dfs(temp * nums[index], index + 1, pl, mi, mu - 1, di)
        if di > 0:
            result = abs(temp) // nums[index]
            if temp < 0:
                result *= -1
            dfs(result, index + 1, pl, mi, mu, di - 1)

dfs(nums[0], 1, plus, minus, mul, div)
print(max(ans))
print(min(ans))

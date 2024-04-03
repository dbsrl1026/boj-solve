n = int(input())
k = int(input())

memo = {}

def dfs(colors, choice):
    if colors <= (choice-1) * 2 or choice < 1:
        return 0
    if (colors, choice) in memo:
        return memo[(colors, choice)]
    if choice == 1:
        memo[(colors, choice)] = colors
        return colors
    else:
        memo[(colors, choice)] = dfs(colors-2, choice-1) + dfs(colors-1, choice)
        return memo[(colors, choice)]
if k ==1:
    answer = n % 1000000003
else:
    answer = (dfs(n-3, k-1) + dfs(n-1, k)) % 1000000003
print(answer)

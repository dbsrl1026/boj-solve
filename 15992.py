test = int(input())
dict = {(0, 0): 1}


def dp(n, m):
    if (n, m) in dict:
        return dict[(n, m)]
    if n < 0 or m < 0:
        return 0
    dict[(n, m)] = dp(n - 1, m - 1) + dp(n - 2, m - 1) + dp(n - 3, m - 1)
    return dict[(n, m)]


for _ in range(test):
    n, m = map(int, input().split())
    print(dp(n, m) % 1000000009)

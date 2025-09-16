n,m = map(int, input().split())
arr = list(map(int, input().split()))

if (n == 1 and m == 2) or (n == 2 and m == 1):
    print("ChongChong")
else:
    print("GomGom")
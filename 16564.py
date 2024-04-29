import sys
input = sys.stdin.readline
n, k = map(int, input().split())
characters = []
for i in range(n):
    characters.append(int(input()))

min_level = min(characters)
max_level = max(characters) + k

while min_level < max_level:
    mid = (min_level+max_level + 1) // 2
    temp = k
    for level in characters:
        if level < mid:
            temp -= mid - level
            if temp < 0:
                break
    if temp < 0:
        max_level = mid -1
    else:
        min_level = mid

print(min_level)
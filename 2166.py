n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

plus = 0
minus = 0
for i in range(n):
    plus += points[i][0] * points[(i + 1) % n][1]
    minus += points[(i + 1) % n][0] * points[i][1]

answer = round(0.5 * abs(plus - minus), 1)
print(answer)

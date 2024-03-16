N = int(input())
point = list(map(int, input().split()))
maxPoint = max(point)
sum = 0
for i ,p in enumerate(point):
    sum += p/maxPoint*100
average = sum / N
print(average)
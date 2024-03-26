n = int(input())
nums = list(map(int, input().split()))
p1 = 0
p2 = n - 1
min = 2000000000
a = 0
b = 0
while p1 != p2:
    temp = nums[p1] + nums[p2]
    if abs(temp) < min:
        min = abs(temp)
        a = nums[p1]
        b = nums[p2]
    elif temp < 0:
        p1 += 1
    else:
        p2 -= 1

print(a, b)

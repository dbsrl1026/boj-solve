def check(nums, target):
    nums_sort = sorted(nums)
    start = 0
    end = len(nums_sort) - 1
    while True:
        if start > end:
            return False
        elif nums_sort[start] + nums_sort[end] == target:
            return True
        elif nums_sort[start] + nums_sort[end] < target:
            start +=1
        elif nums_sort[start] + nums_sort[end] > target:
            end -=1


nums = map(int, input().split())
target = int(input())
ans = check(nums, target)
print(ans)

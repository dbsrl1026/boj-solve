test = int(input())


def divide(arr):
    if len(arr) == 1:
        return True
    mid = (len(arr) - 1) // 2
    left = arr[:mid]
    right = [1 if num == 0 else 0 for num in arr[mid+1:]]
    right.reverse()
    if left != right:
        return False
    else:
        return divide(left) and divide(right)

for _ in range(test):
    arr = list(map(int, list(input())))
    if divide(arr):
        print('YES')
    else:
        print('NO')


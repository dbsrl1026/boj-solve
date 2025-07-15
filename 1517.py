n = int(input())
arr = list(map(int, input().split()))
cnt = 0

def dnq(left, right):
    global cnt
    if left == right:
        return [arr[left]]
    mid = (left + right) // 2
    left_arr = dnq(left, mid)
    right_arr = dnq(mid + 1, right)

    j = 0
    k = 0
    temp = []
    for i in range(len(left_arr)):
        while j < len(right_arr) and left_arr[i] > right_arr[j]:
            temp.append(right_arr[j])
            j += 1
            k += 1
        temp.append(left_arr[i])
        cnt += k - i
        k += 1
    while j < len(right_arr):
        temp.append(right_arr[j])
        j += 1
        k += 1
    return temp

dnq(0, n -1)
print(cnt)





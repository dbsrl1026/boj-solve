l = int(input())
arr = list(input())

lps = [0] * l
j = 0
for i in range(1, l):
    while j != 0 and arr[i] != arr[j]:
        j = lps[j - 1]
    if arr[i] == arr[j]:
        j += 1
        lps[i] = j
print("가장 짧은 광고 길이 :" + str(l - lps[l - 1]))

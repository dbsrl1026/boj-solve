def long(num):
    longest = 0
    dic = {}
    for v in num:
        dic[v] = 1
    for v in num:
        if v-1 not in dic:
            next = v + 1
            cnt =1
            while next in dic:
                #dic[v] += 1
                next += 1
                cnt +=1
            longest = max(longest, cnt)

    return longest
 #   return max(dic.values())


num=[]
num = list(map(int, input().split()))

if len(num) == 0:
    ans = 0
else:
    ans = long(num)
print(ans)
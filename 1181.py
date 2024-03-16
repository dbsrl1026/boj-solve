num = int(input())
dic={}
for i in range(num):
    temp = input()
    if temp not in dic:
        dic[temp] = len(temp)
dic = dict(sorted(dic.items()))
dic = dict(sorted(dic.items(), key= lambda x : x[1]))
for key, value in dic.items():
    print(key)
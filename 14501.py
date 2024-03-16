n = int(input())
time = []
pay = []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

def dfs(day, earn):
    if day == n:
        return earn
    doWork = earn
    if day + time[day] <=n:
        doWork = dfs(day+time[day], earn+pay[day])
    notWork = dfs(day+1, earn)
    if doWork > notWork:
        return doWork
    else:
        return notWork

print(dfs(0,0))
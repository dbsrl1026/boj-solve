L,K,C = map(int,input().split())
cuts = [0,L] + list(map(int,input().split()))
cuts.sort()

def solution(x):
    cnt = 0
    cut_start = L
    prev=[]
    for i in range(len(cuts)-1,-1,-1):
        diff = cuts[i] - cuts[i-1]
        total = cut_start - cuts[i]
        if diff > x:
            return 10001,0
        elif total > x:
            cut_start = cuts[i+1]
            prev.append(cuts[i+1])
            cnt+=1
        else:
            continue

    if cnt < C:
        first = cuts[1]
    else:
        first = prev[-1]

    return cnt, first

lo = 0
hi = L
answer = 0
first_cut = 0
while lo <= hi:
    mid = (lo+hi)//2

    cnt,first = solution(mid)

    if C < cnt:
        lo = mid+1
    else:
        answer=mid
        first_cut = first
        hi = mid-1

print(answer,first_cut)

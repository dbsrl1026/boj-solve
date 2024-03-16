
def findSosu(k):
    if k ==1 :
        return 0
    for i in range(2,int(k**0.5+1)):
        if k%i == 0:
            return 0
    return 1
M,N = map(int,input().split())


for i in range(M, N+1):
    if findSosu(i) == 1:
        print(i)

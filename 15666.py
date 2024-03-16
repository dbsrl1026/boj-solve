n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr = sorted(set(arr))

def dfs(seq, l, last):
    if l == m:
        print(' '.join(map(str,seq)))
        return
    for i in range(last, len(arr)):
        dfs(seq + [arr[i]],l+1, i)
    return

dfs([],0,0)


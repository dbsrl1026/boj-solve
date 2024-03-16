n = int(input())

grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))



def getTotalSynergy(team):
    ssum = 0
    for i in range(int(n / 2)):
        for j in range(int(n / 2)):
            if i != j:
                ssum += grid[team[i]][team[j]]
    return ssum


def dfs(teamA, teamB, k):
    if k == n:
        sa = getTotalSynergy(teamA)
        sb = getTotalSynergy(teamB)
        return abs(sa - sb)
    if len(teamA) == int(n/2):
        return dfs(teamA, teamB + [k], k+1)
    elif len(teamB) == int(n/2):
        return dfs(teamA + [k], teamB, k+1)
    else:
        b1 = dfs(teamA, teamB + [k], k+1)
        b2 = dfs(teamA + [k], teamB, k+1)
        if b1 < b2:
            return b1
        else:
            return b2

print(dfs([0],[],1))
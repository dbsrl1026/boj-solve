from itertools import combinations

n, m, k = map(int, input().split())
quests = [list(map(int, input().split())) for _ in range(m)]
cases = combinations(range(1, 2 * n + 1), n)
maxx = 0

for skills in cases:
    skill_set = set(skills)
    complete = 0
    for quest in quests:
        if all(skill in skill_set for skill in quest):
            complete += 1
    maxx = max(maxx, complete)

print(maxx)
from collections import defaultdict
n, m = map(int, input().split())
vacations = defaultdict(list)
ans = 0
for i in range(n):
    judge = list(map(int, input().split()))
    v = judge[0]
    for j in range(v):
        s = judge[1 + 2*j]
        e = judge[1 + 2*j + 1]
        vacations[i].append((s, e))
for day in range(1, m + 1):
    available = 0
    for vacation in vacations.values():
        gone = False
        for s, e in vacation:
            if s <= day <= e:
                gone = True
                break
        if not gone:
            available += 1
    if available >= 3:
        ans += 1
print(ans)
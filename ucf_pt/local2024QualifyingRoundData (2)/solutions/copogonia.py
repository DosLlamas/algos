
from math import sqrt

n, k, m = map(int, input().split())

pts = [list(map(int, input().split())) for _ in range(n)]
edges = [list(map(int, input().split())) for _ in range(k)]

def dist(a, b):
   dx,dy = a[0]-b[0],a[1]-b[1]
   return sqrt(dx*dx+dy*dy)

dists = [[dist(pts[i], pts[j]) for j in range(n)] for i in range(n)]


ans = 10**20
for mp in range(1<<k):
   arr = [[m + 1]*n for _ in range(n)]
   for i in range(n):
      arr[i][i] = 0
      arr[i][(i+1)%n] = dists[i][(i+1)%n]
      arr[(i+1)%n][i] = dists[(i+1)%n][i]
   tans = 0
   for i in range(k):
      if (mp>>i)&1:
         tans += edges[i][2]
         arr[edges[i][0]-1][edges[i][1]-1] = dists[edges[i][0]-1][edges[i][1]-1]
         arr[edges[i][1]-1][edges[i][0]-1] = dists[edges[i][1]-1][edges[i][0]-1]
   if tans > ans: continue
   for i in range(n):
      for j in range(n):
         for k in range(n):
            arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])
   good = 1
   for i in range(n):
      for j in range(n):
         if arr[i][j] > m:
            good = 0
      if not good: break
   if good: ans = tans
print(ans)



n,m = map(int, input().split())

g = list([int(x) for x in input()] for _ in range(n))
s = [[0]*(m+1) for _ in range(n+1)]

ans = 0
for i in range(1,n+1):
   for j in range(1,m+1):
      s[i][j] = g[i-1][j-1] + s[i-1][j] + s[i][j-1] - s[i-1][j-1]
      for ii in range(i):
         for jj in range(j):
            if s[i][j] - s[ii][j] - s[i][jj] + s[ii][jj] == (i-ii)*(j-jj):
               ans = max(ans, (i-ii)*(j-jj))
 
print(ans)


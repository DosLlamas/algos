
n,m = map(int, input().split())

g = [list(int(x) for x in input()) for _ in range(n)]

hist = [0]*(m+2)

def comp(arr, rev):
   n = len(arr)
   res = [0]*n
   stk = [None]*n
   stk_size = 0
   for ii in range(n):
      i = ii if rev else n-1-ii
      while stk_size and arr[stk[stk_size-1]] >= arr[i]:
         stk_size-=1
      if stk_size:
         if rev:
            res[i] = stk[stk_size-1] + 1
         else:
            res[i] = stk[stk_size-1] - 1
      else:
         res[i] = i
      stk[stk_size] = i
      stk_size+=1
   return res
ans = 0
for i in range(n):
   for j in range(m):
      hist[j+1] = g[i][j]*(hist[j+1] + 1)
   lefts = comp(hist,1)
   rights = comp(hist,0)

   for i in range(m):
      ans = max(ans, hist[i+1]*(rights[i+1]+1-lefts[i+1]))


print(ans)

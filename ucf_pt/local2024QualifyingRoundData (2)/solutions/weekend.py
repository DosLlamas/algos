
L, H = map(int, input().split())

costs = list(map(int, input().split()))
counts = list(map(int, input().split()))

probs = [[[0] * 101 for _ in range(101)] for _ in range(2)]

probs[1][0][0] = 1
ans = 0
for i in range(0,1+counts[0]):
   for j in range(0,1+counts[1]):
      for k in range(0,1+counts[2]):
         if H < i*costs[0] + j*costs[1] + k *costs[2]: break
         
         if i or j or k:
            probs[1][j][k] = 0
            if j: probs[1][j][k] += probs[1][j-1][k] * (counts[1]-(j-1))/(counts[0] + counts[1] + counts[2] - (i+j+k-1))
            if i: probs[1][j][k] += probs[0][j][k] *   (counts[0]-(i-1))/(counts[0] + counts[1] + counts[2] - (i+j+k-1))
            if k: probs[1][j][k] += probs[1][j][k-1] * (counts[2]-(k-1))/(counts[0] + counts[1] + counts[2] - (i+j+k-1))
         

         if L <= i*costs[0] + j*costs[1] + k *costs[2] <= H:
            ans += probs[1][j][k]
            probs[1][j][k] = 0
   probs[1],probs[0] = probs[0],probs[1]

print(ans)

n = int(input())
populations = [int(input()) for _ in range(n)]
t = int(input())
res = []
for _ in range(t):
    transaction = input().split()
    if transaction[0] == 'R': 
        l = int(transaction[1]) - 1  
        r = int(transaction[2])     
        res.append(sum(populations[l:r]))
    else: 
        country = int(transaction[1]) - 1 
        update = int(transaction[2])
        populations[country] += update
for ans in res:
    print(ans)
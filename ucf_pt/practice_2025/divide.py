n, d = map(int, input().split())
solved = []
tps = 0
for i in range(n):
    num = int(input())
    tps += num
    solved.append(num)

r = d // tps

for i in range(n):
    print(solved[i] * r)


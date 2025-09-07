n, r, c = map(int, input().split())
bullseye = (n + 1) // 2
d = max(abs(r - bullseye), abs(c - bullseye))
score = 100 - 10 * d
print(score)
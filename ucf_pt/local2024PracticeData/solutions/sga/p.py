from collections import defaultdict
n = int(input())
first_char = [0]*26
names = defaultdict(int)
for i in range(n):
    name = input()
    first_char[ord(name[0]) - ord('A')] += 1
    names[name] += 1
res = 0
for name in names:
    res += names[name] * (first_char[ord(name[0]) - ord('A')] - names[name])
print(res)

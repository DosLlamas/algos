from collections import Counter

s = input()
s_pairs = sorted(Counter(s).items(), key=lambda pair: (-pair[1], pair[0]))
res = "".join([char*cnt for (cnt, char) in s_pairs])
print(res)
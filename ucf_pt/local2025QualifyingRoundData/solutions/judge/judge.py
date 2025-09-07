# UCF Local Contest 2025 (Qualifying) - Judge Meeting
# Solution written by Tyler Marks

# scan in the number of coaches and days
n, m = map(int, input().split())

# store a frequency array of how many coaches
# are missing each day
frq = [0] * (m+1)

# scan in each coaches vacation time
for i in range(n):
    ranges = list(map(int, input().split()))
    v = ranges[0]
    for j in range(v):
        s = ranges[2*j+1]
        e = ranges[2*j+2]

        # update frq for each day in range
        for k in range(s, e+1):
            frq[k] += 1

# count how many days have enough coaches
res = 0
for i in range(1, m+1):
    if n - frq[i] >= 3:
        res += 1

# output the answer
print(res)
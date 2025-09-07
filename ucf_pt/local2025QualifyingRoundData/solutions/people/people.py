# UCF Local Contest 2025 (Qualifying) - World Population
# Solution written by Tyler Marks

# Fast input
import sys
input = sys.stdin.readline

# Scan in number of countries
n = int(input())

# Initialize a Binary Index Tree
bit = [0] * n

# Increase arr[i] by d in the BIT
def update(i, d):
    global bit
    while i < n:
        bit[i] += d
        i |= i+1

# Query sum of arr[j] s.t. j < i in the BIT
def query(i):
    global bit
    res = 0
    while i > 0:
        res += bit[i-1]
        i &= i-1
    return res

# Scan in the inital populations
for i in range(n):
    v = int(input())
    update(i, v)

# Scan in the number of queries
q = int(input())

# Process each query
for _ in range(q):
    x, y, z = input().split()
    if x == 'U':
        i = int(y)
        d = int(z)
        update(i-1, d)
    else:
        l = int(y)
        r = int(z)
        print(query(r) - query(l-1))
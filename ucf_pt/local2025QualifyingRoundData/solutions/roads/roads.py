# UCF Local Contest 2025 (Qualifying) - Country Roads
# Solution written by Tyler Marks

# Scan in the number of cities, initial roads,
# and candidate roads
n, m, r = map(int, input().split())

# Initialize the DSU array
dsu = [-1] * n

# Auxilary functions for DSU
def find(x):
    global dsu
    if dsu[x] < 0: return x
    dsu[x] = find(dsu[x])
    return dsu[x]

def join(x, y):
    global dsu
    x = find(x)
    y = find(y)
    if x == y: return False
    if dsu[x] > dsu[y]: x, y = y, x
    dsu[x] += dsu[y]
    dsu[y] = x
    return True

# Scan in inital edges and join those nodes
# in the DSU
for i in range(m):
    u, v = map(int, input().split())
    join(u-1, v-1)

# Scan in the candidate edges
new_edges = []
for i in range(r):
    u, v, w = map(int, input().split())
    new_edges.append((w, u-1, v-1))

# Sort the new_edges to perform kruskals algorithm
new_edges = sorted(new_edges)

# Go through each edge, and if the join is
# successful, add the weight to the answer
res = 0
for w, u, v in new_edges:
    if join(u, v):
        res += w

# Output the answer
print(res)
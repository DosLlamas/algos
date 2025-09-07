# UCF Local Contest 2025 (Qualifying) - Who wants to be a Millionaire?
# Solution written by Tyler Marks

# Scan in input
n = int(input())
w = list(map(int, input().split()))
p = list(map(float, input().split()))
q = list(map(float, input().split()))

# Initialize the DP Table
dp = [[0.0 for i in range(3)] for j in range(n+1)]

# BASE CASE: If we hit the last question, we win w[n-1] dollars
dp[n] = [w[-1] for i in range(3)]

# STATE: Current question and how many times we've been helped
for idx in reversed(range(n)):
    for used in range(3):
        # TRANSITION:
        # Cash out
        stop = float(w[idx-1]) if idx > 0 else 0.0
        # Answer the question without help
        self = p[idx] * dp[idx+1][used]
        # Answer the question with help
        expert = q[idx] * dp[idx+1][used+1] if used < 2 else 0.0
        
        # Set the current dp answer to the max of the three choices
        dp[idx][used] = max(stop, self, expert)

# Output the answer with 10 decimal places
print("{:.10f}".format(dp[0][0]))
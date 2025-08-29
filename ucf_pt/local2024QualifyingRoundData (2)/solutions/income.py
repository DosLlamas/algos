# Arup Guha
# 8/2/2024
# Solution to 2024 UCF Locals Qualifying Round Problem: Income Inequality

def solve(money):

    # Sort from big to small.
    n = len(money)
    money.sort(reverse = True)
    tot = sum(money)

    # Our initial answer, running sum.
    res = 0
    curS = 0

    # Loop through rev. sorted incomes.
    for i in range(n):

        # Sum of top i+1 people.
        curS += money[i]

        # This is what we're trying to maximize.
        res = max(res, curS/tot - (i+1)/n)

    # As a percentage.
    return 100*res

# Run it.
n = int(input())
vals = [int(x) for x in input().split()]
print(solve(vals))
    

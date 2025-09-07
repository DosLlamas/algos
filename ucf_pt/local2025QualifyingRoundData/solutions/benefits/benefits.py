# Arup Guha
# Alternate Solution to 2025 UCF Locals Qualifying Problem: Social Security Benefits
# 8/2/2025

# Get input.
toks = input().split()
age1 = int(toks[0])
money1 = int(toks[1])
toks = input().split()
age2 = int(toks[0])
money2 = int(toks[1])
live = int(input())

# All the ways option 1 wins.
if age2 > live or (live-age1)*money1 >= (live-age2)*money2:
    print(1)

# Must be option 2
else:
    print(2)

# Arup Guha
# Alternate Solution to 2025 UCF Locals Qualifying Problem: Single-Elimination Tournament
# 8/2/2025

# Get input.
n = int(input())

# So, take the difference from the highest power of 2 <= to n
# This is the number of teams that advance from prelim to round 1
# So we just need to double that value (left shift by 1).
print( (n - (1<< (n.bit_length()-1) )) << 1 )

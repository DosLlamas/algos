# Arup Guha
# Alternate Solution to 2025 UCF Locals Qualifying Problem: Simplified Dart Game
# 8/2/2025

# Get input.
toks = [int(x) for x in input().split()]
center = (toks[0]+1)//2

# We want the maximum between horizontal or vertical distance to center.
dist = max( abs(center-toks[1]), abs(center-toks[2]) )

# This is the pattern.
print(100 - 10*dist)

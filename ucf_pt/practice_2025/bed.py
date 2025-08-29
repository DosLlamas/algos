import math

res = ""
l, w, h = map(int, input().split())
x, y, angle = map(int, input().split())
# convert angle to radians
rad = math.radians(angle)

# compute feet position
x2 = x + (h * math.cos(rad)) 
y2 = y + (h * math.sin(rad))

# round to nearest integer to avoid floating-point drift
x2 = round(x2, 9)
y2 = round(y2, 9)

# Check feet
if x2 < 0 or x2 > w or y2 < 0 or y2 > l:
    res = "NO"
# Check head
elif x < 0 or x > w or y < 0 or y > l:
    res = "NO"
else:
    res = "YES"

print(res)
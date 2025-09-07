import math
a1, p1 = map(int, input().split())
a2, p2 = map(int, input().split())
e = int(input())

option1 = p1 * math.floor(e - a1)
option2 = p2 * math.floor(e - a2)

if option1 >= option2:
    print(1)
else:
    print(2)
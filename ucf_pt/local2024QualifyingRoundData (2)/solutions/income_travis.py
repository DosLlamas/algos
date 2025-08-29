
# Read in the number of households
n = int(input())

# Total money
total = 0
answer = 0

# Read in the money for each house
arr = list(map(int, input().split()))
total = sum(arr)

# Sort the array
arr.sort()

# Iterate through the houses from wealthiest to poorest
curWealth = 0
for i in range(n):
   x = arr[-(i+1)]
   curWealth += x
   
   answer = max(answer, (curWealth*n - (i+1)*total) / (total * n))

print(answer * 100)

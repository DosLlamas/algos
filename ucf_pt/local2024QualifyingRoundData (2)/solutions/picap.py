
# Read in the number of names and lines
num_names, num_lines = map(int,input().split())

# Read in the length of each name
arr = list(map(int, input().split()))

# Function to check if a line length will work
def canDo(line_len):
   global num_names, arr, num_lines

   # Track how many lines have been used and spot of current line
   curLine = 1
   curLen = -1 # -1 b/c no space on first name of each line

   # Iterate through all the names
   for x in arr:
      # Check if this name is way too big
      if x > line_len: return 0

      # Check if the name won't fit on the current line
      if x + curLen + 1 > line_len:
         curLen = -1
         curLine += 1

      # Update the spot in the current length
      curLen += x + 1

      # Check if too many lines 😥
      if curLine > num_lines: return 0

   # Successfully used all the names!!!
   return 1

# Exponentiate the hi until valid
lo = 0
hi = 1
while not canDo(hi):
   lo = hi
   hi *= 2

# default the answer to this hi value since it works...
ans = hi
hi -= 1

# Search while a value could be tested
while lo <= hi:
   # Find a mid point
   mid = (lo + hi) >> 1

   if canDo(mid):
      ans = mid
      hi = mid - 1
   else:
      lo = mid + 1

# Print the answer we found
print(ans)

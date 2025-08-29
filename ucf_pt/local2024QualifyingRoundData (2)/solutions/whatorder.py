
# Types of clues
AFTER = "1"
BEFORE = "2"
ADJ = "3"

# Read in the acts and clues
num_acts,num_clues = map(int, input().split())

# Read in the clues (add a dummy act to prevent case handling
adj_allowed = [[1]*(num_acts+1) for _ in range(num_acts+1)]

# Cannot follow yourself
for i in range(num_acts): adj_allowed[i][i] = 0 
can_after = [[1]*(num_acts+1) for _ in range(num_acts+1)]
for _ in range(num_clues):
   ty,act1,act2 = input().split()
   act1 = ord(act1) - ord('A')
   act2 = ord(act2) - ord('A')
   if ty == AFTER:
      can_after[act1][act2] = 0
   elif ty == BEFORE:
      can_after[act2][act1] = 0
   else:
      adj_allowed[act1][act2] = 0
      adj_allowed[act2][act1] = 0

# Make the memo table
table = [[0] * (2<<num_acts) for _ in range(num_acts + 1)]
table[num_acts][1<<num_acts] = 1

# Make the answer
ans = 0

# Try all act maps
for i in range((1<<num_acts)+1,2<<num_acts):
   for last in range(num_acts): # current last
      if not ((i>>last) & 1): continue # not valid last act
      for last2 in range(num_acts+1): # second to last
         if not adj_allowed[last][last2]: continue
         if not ((i>>last2) & 1): continue # not valid 2nd to last act
         
         # Check that this act can come before everyone not performed yet
         good = 1
         for last3 in range(num_acts+1):
            if not ((i>>last3) & 1) and not can_after[last][last3]:
               good = 0
         if not good: continue

         # Add previous to answer
         table[last][i] += table[last2][i^(1<<last)]
      
      # Check if all acts were performed
      if i == (2<<num_acts)-1:
         ans += table[last][i]

# Print the answer
print(ans)

# Arup Guha
# Alternate Solution to 2025 UCF Locals Qualifying Problem: Cover Your Bases
# 8/2/2025

# Returns the value of s in base, base. Returns -1 if the representation
# isn't possible.
def getval(s,base):

    val = 0

    # Go through "digits"
    for i in range(len(s)):
        digit = ord(s[i])-ord('0')

        # s can't work in this base.
        if digit >= base:
            return -1

        # Update value.
        val = base*val + digit

    return val
    
# Get input.
toks = input().split()
strX = toks[0]
strY = toks[1]
strS = toks[2]

# Sum we're trying to reach.
target = getval(strS,10)
done = False

# These are the only bases we're supposed to try.
for b1 in range(2,11):
    for b2 in range(2,11):

        # Get the two values in the two bases.
        v1 = getval(strX, b1)
        v2 = getval(strY, b2)

        # Not valid bases...
        if v1 == -1 or v2 == -1:
            continue

        # We got it!
        if v1 + v2 == target:
            print(b1,b2)
            done = True
            break
        
    # So we don't print anymore!
    if done:
        break

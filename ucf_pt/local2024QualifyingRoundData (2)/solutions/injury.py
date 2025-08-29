
# Possible outputs
IN = "1"
CONCAT = "2"
NOT_FOUND = "0"

# Read in the number of words in the dictionary
n = int(input())

# Read in the dictionary of words as a set
dictionary = set(input() for _ in range(n))

# Function to check the status of a word
def go():
    global dictionary
    
    # Read in the word orooji tried to spell
    word = input()

    # Check if the word is in the dictionary
    if word in dictionary:
       print(IN)
    else:
       good = 0
       
       # Look at all possible splits
       for index in range(1,len(word)):
          # Check if both parts of the split are in the dictionary

          if word[:index] in dictionary and word[index:] in dictionary:
             good = 1
       if good:
          print(CONCAT)
       else:
          print(NOT_FOUND)

# Read in the number of words to check
word_to_test_count = int(input())

# Check all the test words
for _ in range(word_to_test_count):
    go()

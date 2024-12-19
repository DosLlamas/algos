""" 
1.
Write an algorithm to find the first unique string (string that only appears once)
in a file of strings. Each string is separated by a space. There may be more than one unique string - return the first 
one that appears left to right. The file is not empty and there is at least one unique string. Use file reading. 
Example:
["apple", "boy", "charlie", "apple"]
 
2.
What data structure would you use to develop a function similar to Google's browser
forward and back page button? How would you keep track of the previous pages while 
blocking the option to hit "forward" on the forward most page.
 """

# 1.
from collections import defaultdict
def find_unique_string(file: str) -> str:
    count = defaultdict(int)
    with open(file, 'r') as f:
        word = ''
        while True:
            char = f.read(1)
            if not char:  # End of file
                if word:  # Add the last word
                    count[word] += 1
                break
            if char.isspace():  # Word delimiter
                if word:
                    count[word] += 1
                    word = ''
            else:
                word += char
    with open(file, 'r') as f:
        word = ''
        while True:
            char = f.read(1)
            if not char:
                if word: 
                    if count[word] == 1: return word
                break
            if char.isspace(): 
                if word:
                    if count[word] == 1: return word
                    word = ''
            else:
                word += char
print(find_unique_string('words.txt'))

# 2.
"""
I would use a doubly linked list to keep track of the previous pages. I would also keep track of the current page.
To block the option to hit "forward" on the forward most page, I would keep a pointer to the current page. If the user
hits the "forward" button, I would check if the current page is the last page in the linked list. If it is, I would not
allow the user to go forward. If the user goes back, I would update the current page to the previous page and update the
linked list accordingly.
"""
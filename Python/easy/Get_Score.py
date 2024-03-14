"""
Paul's question:
There is a string of binary numbers:
# binary = '11111111.11111110.10101010.00000001'

For this string, count the number of 
total ones and keep a score like so:

0-0
1-1
2-2
3-4
4-8
5-16
...

Return the score
and 1 count for each set
of binary numbers
...

Approach 1, naive approach:
Thoughts:
I need a way to count the number of
1s but also the score.
What is a good data structure
for this goal?
I stored all of the values in a tuple inside a list
so I could append data dynamically to a list.
Steps:
1.
Split "str" into a list
2.
declare count variable, set to 0
3.
declare score variable, set to 0
4.
Iterate through str, counting 1s and keeping score
5.
return results
"""
from math import floor
def get_score(str):
    sections_of_binaries = str.split(".")
    counts_and_scores = []
    for index, binary in enumerate(sections_of_binaries):
        count = 0
        score = 0
        for char in binary:
            if char == "1" :
                count += 1
                score = floor((2**(count-4)*8))
        counts_and_scores.append((f'Binary Set #: {index+1}', f'Count: {count}', f'Score: {score}'))
    
    return counts_and_scores

# binary = '11111111.11111110.10101010.00000001'
# print(get_score(binary))

""""
Tradeoffs:
With this approach, the time complexity is
O(n**2) due to the nested for loops and need
to iterate through the string once to split it 
into a sequence.
I'm thinking there is a way to get the count
and score in a dictionary all in one pass
at O(n) time with the use of a dict.
How can I do that?
"""
def get_score2(str):
    sections_of_binaries = str.split(".")
    counts_and_scores = {}
    for index, binary in enumerate(sections_of_binaries):
        count = 0
        score = 0
        for char in binary:
            if char == "1" :
                count += 1
        score = floor((2**(count-4)*8))
        counts_and_scores[f'Binary#{index+1}'] = {
            'count': count,
            'score': score
        }
    
    return counts_and_scores
binary = '11111111.11111110.10101010.00000001'
# print(get_score2(binary))
# print(get_score2(binary)['Binary#3'])
result = get_score2(binary)
print(result)
# print(result['Binary#3'])
    

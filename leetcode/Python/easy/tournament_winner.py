"""
There's an algorithms tournament taking place in which teams of programmers
compete against each other to solve algorithmic problems as fast as possible.
Teams compete in a round robin, where each team faces off against all other
teams. Only two teams compete against each other at a time, and for each
competition, one team is designated the home team, while the other team is the
away team. In each competition there's always one winner and one loser; there
are no ties. A team receives 3 points if it wins and 0 points if it loses. The
winner of the tournament is the team that receives the most amount of points.

Given an array of pairs representing the teams that have competed against each
other and an array containing the results of each competition, write a
function that returns the winner of the tournament. The input arrays are named
"competitions" and "results". The competitions array has elements in the form of
"[homeTeam, awayTeam]", where each team is a string of at most 30 characters
respresting the name of the team. The "results" array contains info
about the winner of each corresponding competion in the "competitions" array. 
Specifically, results[i] denotes the winner of the competitions[i], where a "1"
in results array means that the home team in the corresponding competition won 
and a "0" means that the away team won.

It's guaranteed that exactly one team will win the tournament and that each
team will compete against all other teams exactly once. It's also guaranteed
that the tournament will always have at least two teams.

Sample input:
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]


Sample output:
"Python"


Steps:
1. 
create dict to hold scores for teams
2.
iterate through results
3.
for each, get the corresponding index from competions, then add points to appropiate team
4.
return team with most points

Complexity:
O(n + m) time | O(m) space where m is number of teams in scores dict
"""
# My finished approach
# def tournamentWinner(competitions, results):
#     scores = {}
#     for index, result in enumerate(results):
#         if result == 1:
#             scores[competitions[index][0]] = scores.get(competitions[index][0], 0) + 3
#         else:
#             scores[competitions[index][1]] = scores.get(competitions[index][1], 0) + 3
    
#     return max(scores, key=scores.get)


# Chatgpt's more efficient answer: O(n) time | O(m) space where m is number of unique teams in scores dict
# def tournamentWinner(competitions, results):
#     scores = dict()
#     current_leader = None
#     max_score = 0

#     for index, result in enumerate(results):
#         if result == 1:
#             winning_team = competitions[index][0] 
#         else:
#             winning_team = competitions[index][1]
#         scores[winning_team] = scores.get(winning_team, 0) + 3

#         if scores[winning_team] > max_score:
#             max_score = scores[winning_team]
#             current_leader = winning_team

#     return current_leader


# competitions = [
#     ["HTML", "C#"],
#     ["C#", "Python"],
#     ["Python", "HTML"],
# ]
# results = [0, 0, 1]

# print(tournamentWinner(competitions, results))



"""
Abstractions of What I learned:

1) Using built-in dictionary methods
    I learned the get() built in method before but forgot how to use
    it for this problem. 

    It take in a dictionary and key value and default value, like so:
    dictionary.get(key, default_value)

    The default value is optional and the method will return None if no key is found.
    In this problem this is used to avoid getting and error when adding a team
    to the scores dictionary. 

    There's other built-in dictionary methods in python, e.g.:
    pop(): Returns the value associated with a specified key and removes 
    that key-value pair from the dictionary. If the key is not found, the method returns a default value.

    clear(): empties out dict

    items(): Returns all the keys in a dictionary and their associated values as a sequence of tuples

    keys(): Returns all the keys in a dictionary as a sequence of tuples.

    values(): Returns all the values in the dictionary as a sequence of tuples.

    popitem(): Returns, as a tuple, the key-value pair 
    that was last added to the dictionary. The method also 
    removes the key-value pair from the dictionary.

2) Using elements from a list or keys/values from an object to access another object's keys
    A line like this to set the value of a key that may or may not have already been 
    declared, but using another object or list as the value being accessed:
    scores[competitions[index][0]] = scores.get(competitions[index][0], 0) + 3

3) The concept of having a current_leader and max_score 
    The idea can be applied to various problems, especially when 
    you need to keep track of the maximum or minimum value encountered so 
    far while iterating through a list or processing a sequence of elements. 

    e.g.:
    Finding the Maximum/Minimum Element in a List:
    Initialize max_element and min_element to the first element of the list.
    Iterate through the list, and for each element, update max_element and 
    min_element if the current element is greater than max_element or smaller
    than min_element, respectively. 

    Finding the Most Frequent Element in a List:
    Use a dictionary to store the count of each element in the list.
    Initialize current_leader and max_count to None and 0, respectively.
    Iterate through the list, updating the counts in the dictionary.
    Keep track of the element with the highest count (current_leader) and its count (max_count) during the iteration.

    Tracking Progress in a Loop:
    Suppose you have a loop that performs some operation on a list of elements, 
    and you want to track the progress by showing the element that has the maximum 
    score or progress so far. Initialize current_leader and max_score to None and 0, respectively.
    During each iteration, update current_leader and max_score based on the progress of the current element.

    Finding the Most Profitable Investment:
    Given a list of investments with their corresponding profits, you can 
    find the investment that yields the highest profit using current_leader and max_profit.
    Initialize current_leader and max_profit to None and 0, respectively.
    Iterate through the investments, updating current_leader and max_profit based on the profit of the current investment.
"""

"""
There's an algorithms tournament taking place in which teams of programmers
compete against each other to solve algorithmic problems as fast as possible.
Teams compete in a round robin, where each team faces off against all other
teams. Only two teams compete against each other at a time, and for each
competition, one team is designated the home team, while the other team is the
away team. In each competition there's always one winner and one loser; there
are no ties. A team receives 3 points if it wins and 0 points if it loses. The
winner of the tournament is the team that receives the most amount of points.

Given an array of pairs representing the teams that have competed against each
other and an array containing the results of each competition, write a
function that returns the winner of the tournament. The input arrays are named
"competitions" and "results". The competitions array has elements in the form of
"[homeTeam, awayTeam]", where each team is a string of at most 30 characters
respresting the name of the team. The "results" array contains info
about the winner of each corresponding competion in the "competitions" array. 
Specifically, results[i] denotes the winner of the competitions[i], where a "1"
in results array means that the home team in the corresponding competition won 
and a "0" means that the away team won.

It's guaranteed that exactly one team will win the tournament and that each
team will compete against all other teams exactly once. It's also guaranteed
that the tournament will always have at least two teams.

Sample input:
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]


Sample output:
"Python"

New attempt - Nov. 19th, 2023

-Input: results and competitions array.
-Output: a string for the winning team

what we know:
-we want to return the team with the most points
-there are no ties
-a win scores 3 points a loss scores 0 points
-a 1 means first time won, a 0 means second team won

what we don't know:
-loop? yes
-dict? yes
-counter?


steps:
1. 
declare dict to keep track of scores, and a variable to keep track of winner
2.
iterate results array adding the scores to the teams in the dict.
on each iteration, assign a winning team and compare it to the current winner
3.
return
winner
"""


def tournamentWinner(competitions, results):
    team_scores = dict()
    tourn_winner = ""
    if results[0] == 0:
        tourn_winner = competitions[0][1]
    elif results[0] == 1:
        tourn_winner = competitions[0][0]

    for index, result in enumerate(results):
        current_winner = ""
        if result == 0:
            current_winner = competitions[index][1]
        else:
            current_winner = competitions[index][0]

        team_scores[current_winner] = team_scores.get(current_winner, 0) + 3
        if team_scores[current_winner] > team_scores[tourn_winner]:
            tourn_winner = current_winner

    return {"winner": tourn_winner, "score": team_scores[tourn_winner]}
        

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]

output = tournamentWinner(competitions, results)
print(output)
print("Winner:", output["winner"])
print("Their score:", output["score"])

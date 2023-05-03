"""
Write a function, has_path that takes in an object representing the adjaceny list
of a directed acyclic graph and two nodes (src, dst). The function should return
a boolean indicating whether or not there exists a direct path between the source
and destination nodes. 
Apprach #1 DFS using recursion:
Steps:
1.
if src == dst return True
2.
check if there is a path through neighbors to dst & return True
3.
return false if no path found
"""

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

# def has_path(graph, src, dst):
#     if src == dst : return True
#     for neighbor in graph[src] :
#         if has_path(graph, neighbor, dst) == True :
#             return True
#     return False

# print(has_path(graph, 'f', 'k'))

"""
Apprach #2 BFS:
Steps:
1.
initalize a queue with src
2.
iterate over queue while not empty
3.
set current queue
4.
check if current is dst & return True
5.
iterate over neighbors to src
6.
add next queue
7.
return False if no path found
"""

# def has_path(graph, src, dst):
#     queue = [src]
#     while len(queue) > 0 :
#         # pop() in python is the same as shift() in JS
#         current = queue.pop(0)
#         if current == dst : return True
#         for neighbor in graph[current] :
#             # append() in python is the same as push() in JS
#             queue.append(neighbor)
#     return False

# print(has_path(graph, 'f', 'k'))

"""
Tradeoffs:
Between DFS and BFS in this problem what are the tradeoffs?
Or even for DFS alone, can I use iteration instead of recursion?
Time/Space complexity
"""
        

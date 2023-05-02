"""
Write a function, has_path that takes in an object representing the adjaceny list
of a directed acyclic graph and two nodes (src, dst). The function should return
a boolean indicating whether or not there exists a direct path between the source
and destination nodes.
"""
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

def has_path(graph, src, dst):
    pass
        

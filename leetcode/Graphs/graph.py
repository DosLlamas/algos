
from collections import defaultdict
class UndirectedGraph: # adjacency list using dictionary. Not adjacency matrix
    def __init__(self):
        # Initialize an empty graph (adjacency list)
        self.graph = defaultdict(list)

    def is_empty(self):
        # Checks if the graph is empty (no nodes)
        return len(self.graph) == 0
    
    def get_node_count(self):
        return len(self.graph)
    
    def get_edge_count(self):
        count = 0
        for node in self.graph:
            count += len(self.graph[node])
        return count
    
    def is_edge_between(self, node1, node2):
        for node in self.graph[node1]:
            return True if node == node2 else False
        
    def add_node(self, node):
        self.graph[node] = []

    def remove_node(self, node):
        for n in self.graph:
            if node in self.graph[n]:
                self.graph[n].remove(node)
        self.graph.pop(node)
    
    def print_graph(self):
        # Prints the adjacency list of the graph
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")
    
    def add_edge(self, node1, node2):
        # Adds an edge between node1 and node2
        self.graph[node1].append(node2)
        self.graph[node2].append(node1) 

# Example Usage
g = UndirectedGraph()

# Check if the graph is empty
print("Is graph empty?", g.is_empty())  # Should return True

# Get number of nodes
print("Node count: ", g.get_node_count())

# Adding some edges
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

# Check if the graph is empty again
print("Is graph empty?", g.is_empty())  # Should return False

# Print the graph
g.print_graph()

# Get number of nodes
print("Node count: ", g.get_node_count())
# Get number of edges
print("Edge count: ", g.get_edge_count())

# Add node
print("Add node 4: ", g.add_node(4))

# Print the graph
g.print_graph()

# Remove node
print("Remove node 1", g.remove_node(1))

# Print the graph
g.print_graph()


class DirectedGraph:  # adjacency list using dictionary. Not adjacency matrix
    def __init__(self):
        # Initialize an empty graph (adjacency list)
        self.graph = {}

    def add_edge(self, node1, node2):
        # Adds a directed edge from node1 to node2
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

        # Ensure node2 is also present in the graph, even if it has no outgoing edges
        if node2 not in self.graph:
            self.graph[node2] = []

    def is_empty(self):
        # Checks if the graph is empty (no nodes)
        return len(self.graph) == 0

    def print_graph(self):
        # Prints the adjacency list of the graph
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    def has_edge(self, node1, node2):
        # Checks if there's a directed edge from node1 to node2
        return node2 in self.graph.get(node1, [])

    def get_outgoing_edges(self, node):
        # Returns a list of nodes that have an edge from the given node
        return self.graph.get(node, [])

    def get_incoming_edges(self, node):
        # Returns a list of nodes that have edges pointing to the given node
        incoming = []
        for n in self.graph:
            if node in self.graph[n]:
                incoming.append(n)
        return incoming

# # Example usage
# g = DirectedGraph()

# # Check if the graph is empty
# print("Is graph empty?", g.is_empty())  # Should return True

# # Adding some directed edges
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(3, 2)

# # Check if the graph is empty again
# print("Is graph empty?", g.is_empty())  # Should return False

# # Print the graph
# g.print_graph()

# # Check if there's a directed edge from 1 to 2
# print("Does an edge exist from 1 to 2?", g.has_edge(1, 2))  # Should return True
# print("Does an edge exist from 2 to 1?", g.has_edge(2, 1))  # Should return False

# # Get outgoing edges for a node
# print("Outgoing edges from node 1:", g.get_outgoing_edges(1))  # Should return [2, 3]

# # Get incoming edges for a node
# print("Incoming edges for node 2:", g.get_incoming_edges(2))  # Should return [1, 3]
# Graphs

# Ideal data structure for modeling networks
# There's vertices (nodes) nd edges
# It can be undirected (bidirectional edges), or directed (unidirectional edges)
# It can be connected (you can relate all nodes through some path)
# It can be weighted (each node has a specified weight)

# It can be represented with an adjacency matrix, which offers O(1) time complexity to find out if 2 nodes are adjacent, but takes O(N^2) space
# where N is the number of vertices

# It can also be represented with an adjancency list, (an array of linked lists), O(Vertices) for accesses, and O(Vertices+Edges) for size


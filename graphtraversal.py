# This is an implementation of Graph Traversal
# Graph traversal means systematically visiting each node in a graph.
# 1. Breadth-First Search (BFS)
# 2. Depth-First Search (DFS)


# Graphs: Big O
# For both DFS and BFS, the time complexity is  O(V+E) where V is the number of vertices, 
# and E is the number of edges.
# 
# This is because both algorithms visit each vertex and edge once. 
# For both DFS & BFS, space complexity is O(V) where V is the number of vertices.

from collections import deque

def bfs(graph, start):
    '''Breadth-First Search'''
    visited = set()
    queue = deque([start])
    visited.add(start)
    #result = []

    while queue:
        current_vertex = queue.popleft()
        print(current_vertex, end = ' ')
        # result.append(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    # return result


#Graph Depth-First Search 
# DFS explores as far as possible along each branch before backtracking.

def dfs(graph, start, visited=None):
    '''Depth-First Search'''
    if visited is None:
        visited = set()

    print(start, end = '')
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


#Alternative 

def dfs2(graph, start, visited=None, result=None):
    '''Depth_first search'''
    # Implement this function
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    
    print(start, end = ' ')
    result.append(start)
    visited.add(start)
        
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs2(graph, neighbor, visited, result)
    return result
    

# Leet-code Challenge - Find if Path Exists in Graph
# There is a bi-directional graph with n vertices, 
# where each vertex is labeled from 0 to n - 1 (inclusive). 
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. 
# Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.


def bfs2(graph, start, destination):
    '''Breadth-First Search'''
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current_vertex = queue.popleft()
        if current_vertex == destination:
            return True
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def valid_path(n, edges, source, destination):
    '''Valid Path Solution'''
    graph = {}
    for i in range(n):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        
    return bfs2(graph, source, destination)


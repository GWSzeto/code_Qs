"""
various implementations of DFS and BFS
heavily makes use of set notation, like set difference, uniquness and what
not
"""

# DFS
# it utlizes a stack as the nodes to be visited next, given its not in the
# visited already
# understanding of how it works in code
def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        vector = stack.pop()
        if vector not in visited:
            visited.append(vector)
            stack.extend(graph[vector] - visited)
        
    return visited

# recursive version
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.append(start)
    for vector in graph[start] - visited:
        if vector not in visited:
            dfs(graph, vector, visited)
    return visited

# finds all possible paths from start to goal
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_vertex in graph[vertex] - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            stack.append((next, path + [next]))

# recursive version of above
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = set()
    if start == goal:
        yield path
    for vector in graph[start] - set(path):
        yield from dfs(graph, vector, goal, path + [vector])


# BFS
# exact same as above, except for the recursive form, but instead of 
# a stack, it uses a queue to store the vectors to visit next
# understanding of how it works
def BFS(graph, start):
    visited = []
    queue = [start]
    while queue:
        vector = queue.pop(0)
        if vector not in visited:
            visited.append(vector)
            queue.extend(graph[vector] - visited)

    return visited

# all the paths from start to goal
# neat thing is, if the graph is unweighted and undirected, the first
# path given is the shortest one
def BFS_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_vertex in graph[vector] - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            queue.append((next_vertex, path + [next_vertex]))

# So a good thing to come out of this is that you can just find
# the shortest path right away
def shortest_path(graph, start, goal):
    try:
        return next(shortest_path(graph, start, goal))
    except StopIteration:
        return None



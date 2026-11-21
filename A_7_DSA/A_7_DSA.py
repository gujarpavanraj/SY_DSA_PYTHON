# DFS using Adjacency Matrix

def DFS(graph, visited, vertex, n):
    print(vertex, end=" ")
    visited[vertex] = 1

    for i in range(n):
        if graph[vertex][i] == 1 and visited[i] == 0:
            DFS(graph, visited, i, n)


# Input number of vertices
n = int(input("Enter number of vertices: "))

# Create adjacency matrix
graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = []
    for j in range(n):
        value = int(input("Enter value for [" + str(i) + "][" + str(j) + "]: "))
        row.append(value)
    graph.append(row)

# Create visited array
visited = []

for i in range(n):
    visited.append(0)

# Starting vertex
start = int(input("Enter starting vertex: "))

# DFS Traversal
print("DFS Traversal:")
DFS(graph, visited, start, n)
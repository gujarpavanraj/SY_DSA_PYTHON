# Graph Representation and Minimum Spanning Tree
# Using Kruskal's and Prim's Algorithms

INF = 999999


# Function to create adjacency matrix
def create_graph():
    V = int(input("Enter number of vertices: "))

    graph = [[0 for j in range(V)] for i in range(V)]

    print("Enter adjacency matrix (0 for no edge):")

    for i in range(V):
        for j in range(V):
            graph[i][j] = int(input())

    return V, graph


# Kruskal's Algorithm
def kruskal(V, graph):
    edges = []

    # Create edge list from adjacency matrix
    for i in range(V):
        for j in range(i + 1, V):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    # Sort edges by increasing weight
    edges.sort()

    # Initialize parent array
    parent = [i for i in range(V)]

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    count = 0
    total = 0

    print("\nKruskal's Minimum Spanning Tree:")

    for w, u, v in edges:
        ru = find(u)
        rv = find(v)

        # Check whether edge creates a cycle
        if ru != rv:
            print(u, "-", v, ":", w)

            parent[ru] = rv

            total = total + w
            count = count + 1

        if count == V - 1:
            break

    if count == V - 1:
        print("Total minimum cost:", total)
    else:
        print("Graph is disconnected. MST cannot be formed.")


# Prim's Algorithm
def prim(V, graph):
    key = [INF] * V
    visited = [False] * V
    parent = [-1] * V

    # Starting vertex
    key[0] = 0

    total = 0

    print("\nPrim's Minimum Spanning Tree:")

    # Repeat V times
    for _ in range(V):

        # Select unvisited vertex with minimum key
        u = -1
        minimum = INF

        for v in range(V):
            if not visited[v] and key[v] < minimum:
                minimum = key[v]
                u = v

        if u == -1:
            print("Graph is disconnected. MST cannot be formed.")
            return

        visited[u] = True

        # Update key and parent of adjacent vertices
        for v in range(V):
            if (graph[u][v] != 0 and
                    not visited[v] and
                    graph[u][v] < key[v]):

                key[v] = graph[u][v]
                parent[v] = u

    # Display MST edges and calculate total cost
    for v in range(1, V):
        print(parent[v], "-", v, ":", key[v])
        total = total + key[v]

    print("Total minimum cost:", total)


# Main Program
V, graph = create_graph()

kruskal(V, graph)

prim(V, graph)
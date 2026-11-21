
class Graph:
    def __init__(self):
        self.vertices = 0
        self.adjacencyList = []

    # Create Graph Using Adjacency List
    def CreateGraph(self):
        self.vertices = int(input("Enter number of users: "))

        # Initialize adjacency list
        self.adjacencyList = [[] for i in range(self.vertices)]

        # Read number of friendships
        edges = int(input("Enter number of friendships: "))

        # Read and insert each friendship
        for i in range(edges):
            source = int(input("Enter user1: "))
            destination = int(input("Enter user2: "))

            # Add destination to source's list
            self.adjacencyList[source].append(destination)

            # Add source to destination's list
            self.adjacencyList[destination].append(source)

    # Display Graph
    def DisplayGraph(self):
        for i in range(self.vertices):
            print(i, " -> ", end=" ")

            # Display connected vertices
            for j in self.adjacencyList[i]:
                print(j, end=" ")

            print()

    # BFS for Social Network
    def BFS(self, startUser):
        # Mark all users as unvisited
        visited = [False] * self.vertices

        # Create an empty queue
        queue = []

        # Mark selected user as visited
        visited[startUser] = True

        # Add selected user to queue
        queue.append(startUser)

        print("Users connected level by level:")

        # Process users until queue is empty
        while queue:
            # Remove the first user
            currentUser = queue.pop(0)

            # Display current user
            print(currentUser, end=" ")

            # Check all friends of current user
            for friend in self.adjacencyList[currentUser]:

                # Check whether friend is already visited
                if visited[friend] == False:

                    # Mark friend as visited
                    visited[friend] = True

                    # Add friend to queue
                    queue.append(friend)

        print()

# Menu-Driven Main Algorithm
def Main():
    # Create an object of Graph class
    socialNetwork = Graph()

    # Initialize menu choice
    choice = 0

    # Repeat menu until user selects Exit
    while choice != 4:
        print("\n===== SOCIAL NETWORK =====")
        print("1. Create Graph")
        print("2. Display Adjacency List")
        print("3. Perform BFS")
        print("4. Exit")

        # Read user's choice
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Create the social network
            socialNetwork.CreateGraph()

        elif choice == 2:
            # Display friendship connections
            socialNetwork.DisplayGraph()

        elif choice == 3:
            # Read the starting user
            startUser = int(input("Enter starting user: "))

            # Perform BFS
            socialNetwork.BFS(startUser)

        elif choice == 4:
            # Terminate the program
            print("Program terminated.")

        else:
            # Handle invalid choice
            print("Invalid choice.")

Main()
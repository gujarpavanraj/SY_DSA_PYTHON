class HeapSort:

    def __init__(self):
        self.score = []

    # Step 1: Read player scores
    def input(self):
        n = int(input("Enter number of players: "))

        for i in range(n):
            s = int(input(f"Enter score of player {i + 1}: "))
            self.score.append(s)

    # Display original scores
    def display(self):
        print("Player Scores:", self.score)

    # Max Heapify
    def maxHeapify(self, a, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Compare left child with current largest
        if left < n and a[left] > a[largest]:
            largest = left

        # Compare right child with current largest
        if right < n and a[right] > a[largest]:
            largest = right

        # Exchange parent with larger child
        if largest != i:
            a[i], a[largest] = a[largest], a[i]

            # Continue heapification
            self.maxHeapify(a, n, largest)

    # Heap Sort using Max Heap
    # Result: Ascending Order
    def maxHeapSort(self):
        a = self.score.copy()
        n = len(a)

        # Step 1: Build Max Heap
        for i in range(n // 2 - 1, -1, -1):
            self.maxHeapify(a, n, i)

        # Step 2: Move maximum element to the end
        for i in range(n - 1, 0, -1):

            # Root contains maximum element
            a[0], a[i] = a[i], a[0]

            # Restore Max Heap property
            self.maxHeapify(a, i, 0)

        # Step 3: Display sorted scores
        print("Player Scores in Ascending Order:", a)

    # Min Heapify
    def minHeapify(self, a, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Compare left child with current smallest
        if left < n and a[left] < a[smallest]:
            smallest = left

        # Compare right child with current smallest
        if right < n and a[right] < a[smallest]:
            smallest = right

        # Exchange parent with smaller child
        if smallest != i:
            a[i], a[smallest] = a[smallest], a[i]

            # Continue heapification
            self.minHeapify(a, n, smallest)

    # Heap Sort using Min Heap
    # Result: Descending Order
    def minHeapSort(self):
        a = self.score.copy()
        n = len(a)

        # Step 1: Build Min Heap
        for i in range(n // 2 - 1, -1, -1):
            self.minHeapify(a, n, i)

        # Step 2: Move minimum element to the end
        for i in range(n - 1, 0, -1):

            # Root contains minimum element
            a[0], a[i] = a[i], a[0]

            # Restore Min Heap property
            self.minHeapify(a, i, 0)

        # Step 3: Display sorted scores
        print("Player Scores in Descending Order:", a)


# Main Algorithm - Menu Driven
def main():

    # Step 1: Create HeapSort object
    leaderboard = HeapSort()

    # Step 2: Enter player scores
    leaderboard.input()

    # Step 3: Display ranking menu
    while True:
        print("\n----- Heap Sort Menu -----")
        print("1. Display Scores")
        print("2. Heap Sort using Max Heap")
        print("3. Heap Sort using Min Heap")
        print("4. Exit")

        # Step 4: Read choice
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Display original scores
            leaderboard.display()

        elif choice == 2:
            # Use Max Heap
            # Result: Ascending Order
            leaderboard.maxHeapSort()

        elif choice == 3:
            # Use Min Heap
            # Result: Descending Order
            leaderboard.minHeapSort()

        elif choice == 4:
            # End the program
            print("Program terminated.")
            break

        else:
            # Handle invalid choice
            print("Invalid choice.")


# Call main function
if __name__ == "__main__":
    main()
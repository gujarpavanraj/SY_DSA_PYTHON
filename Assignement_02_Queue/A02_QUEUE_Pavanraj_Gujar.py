# QUEUE USING ARRAY

class Queue:

    def __init__(self, size):

        self.size = size

        # Creating array
        self.queue = [None] * size

        self.front = -1
        self.rear = -1


    # Enqueue
    def enqueue(self, customer):

        if self.rear == self.size - 1:
            print("Queue is full.")
            return

        if self.front == -1:
            self.front = 0

        self.rear = self.rear + 1

        self.queue[self.rear] = customer

        print("Customer added.")


    # Dequeue
    def dequeue(self):

        if self.front == -1:
            print("Queue is empty.")
            return

        print("Customer served:", self.queue[self.front])

        self.queue[self.front] = None

        self.front = self.front + 1

        if self.front > self.rear:
            self.front = -1
            self.rear = -1


    # Display
    def display(self):

        if self.front == -1:
            print("Queue is empty.")
            return

        print("Customers in queue:")

        i = self.front

        while i <= self.rear:

            print(self.queue[i])

            i = i + 1


# ---------------- MAIN PROGRAM ----------------

size = int(input("Enter maximum size of queue: "))

q = Queue(size)


# Ask how many customers should initially be inserted
n = int(input("Enter number of customers initially: "))

if n > size:
    print("Number of customers cannot be greater than queue size.")

else:

    i = 1

    while i <= n:

        customer = input("Enter customer " + str(i) + ": ")

        q.enqueue(customer)

        i = i + 1


# Operations
while True:

    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        customer = input("Enter customer name: ")

        q.enqueue(customer)

    elif choice == 2:

        q.dequeue()

    elif choice == 3:

        q.display()

    elif choice == 4:

        print("Program ended.")
        break

    else:

        print("Invalid choice.")
# STACK USING OUR OWN NODE

class Node:
    def __init__(self, book):
        self.book = book
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    # Push
    def push(self, book):
        new_node = Node(book)

        new_node.next = self.top
        self.top = new_node

        self.count = self.count + 1

        print("Book added to stack.")

    # Pop
    def pop(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("Book arranged:", self.top.book)

            self.top = self.top.next
            self.count = self.count - 1

    # Peek
    def peek(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("Top book:", self.top.book)

    # Display
    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            temp = self.top

            print("Stack:")

            while temp is not None:
                print(temp.book)
                temp = temp.next


# ---------------- MAIN PROGRAM ----------------

stack = Stack()

# Ask user how many elements are required
n = int(input("Enter number of books initially: "))

# Create initial stack
i = 1

while i <= n:
    book = input("Enter book " + str(i) + ": ")
    stack.push(book)
    i = i + 1


# Operations
while True:

    print("\n----- STACK MENU -----")
    print("1. Return Book (Push)")
    print("2. Arrange Book (Pop)")
    print("3. Top Book (Peek)")
    print("4. Display Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        stack.push(book)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
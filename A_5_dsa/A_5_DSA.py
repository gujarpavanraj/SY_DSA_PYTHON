# Assignment 5A
# Binary Search Tree
# Inorder and Preorder Non-Recursive Traversal


# ---------------- NODE ----------------

class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


# ---------------- STACK NODE ----------------

class StackNode:

    def __init__(self, data):

        self.data = data
        self.next = None


# ---------------- OUR OWN STACK ----------------

class Stack:

    def __init__(self):

        self.top = None


    # Push

    def push(self, data):

        new_node = StackNode(data)

        new_node.next = self.top

        self.top = new_node


    # Pop

    def pop(self):

        if self.top is None:

            return None

        else:

            data = self.top.data

            self.top = self.top.next

            return data


    # Check whether stack is empty

    def is_empty(self):

        if self.top is None:

            return True

        else:

            return False


# ---------------- BINARY SEARCH TREE ----------------

class BST:

    def __init__(self):

        self.root = None


    # Insert node

    def insert(self, data):

        new_node = Node(data)


        # If tree is empty

        if self.root is None:

            self.root = new_node

            return


        temp = self.root


        while True:

            # Insert on left side

            if data < temp.data:

                if temp.left is None:

                    temp.left = new_node

                    return

                else:

                    temp = temp.left


            # Insert on right side

            elif data > temp.data:

                if temp.right is None:

                    temp.right = new_node

                    return

                else:

                    temp = temp.right


            # Duplicate value

            else:

                print("Duplicate value not inserted.")

                return


    # ---------------- INORDER ----------------
    # Left -> Root -> Right
    # Non-Recursive

    def inorder(self):

        if self.root is None:

            print("Tree is empty.")

            return


        stack = Stack()

        current = self.root


        print("Inorder Traversal:")


        while current is not None or not stack.is_empty():

            # Go to the leftmost node

            while current is not None:

                stack.push(current)

                current = current.left


            # Get node from stack

            current = stack.pop()

            print(current.data, end=" ")


            # Move to right subtree

            current = current.right


        print()


    # ---------------- PREORDER ----------------
    # Root -> Left -> Right
    # Non-Recursive

    def preorder(self):

        if self.root is None:

            print("Tree is empty.")

            return


        stack = Stack()

        stack.push(self.root)


        print("Preorder Traversal:")


        while not stack.is_empty():

            current = stack.pop()

            print(current.data, end=" ")


            # Push right first

            if current.right is not None:

                stack.push(current.right)


            # Push left second

            if current.left is not None:

                stack.push(current.left)


        print()


# ---------------- MAIN PROGRAM ----------------

tree = BST()


print("===== BINARY SEARCH TREE =====")

n = int(input("Enter number of nodes: "))


i = 1

while i <= n:

    value = int(input("Enter value for node " + str(i) + ": "))

    tree.insert(value)

    i = i + 1


# ---------------- MENU ----------------

while True:

    print("\n----- BST MENU -----")

    print("1. Inorder Traversal")
    print("2. Preorder Traversal")
    print("3. Exit")


    choice = int(input("Enter your choice: "))


    if choice == 1:

        tree.inorder()


    elif choice == 2:

        tree.preorder()


    elif choice == 3:

        print("Program ended.")

        break


    else:

        print("Invalid choice.")
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, node):
        self.stack.append(node)
        self.top = self.top + 1

    def pop(self):
        if self.top == -1:
            return None

        node = self.stack[self.top]
        self.stack.pop()
        self.top = self.top - 1
        return node

    def is_empty(self):
        if self.top == -1:
            return True
        return False


# Insert a node into BST
def insert(root, value):

    # If tree is empty
    if root is None:
        new_node = Node(value)
        return new_node

    # Insert into left subtree
    if value < root.data:
        root.left = insert(root.left, value)

    # Insert into right subtree
    elif value > root.data:
        root.right = insert(root.right, value)

    # Duplicate values are not allowed
    else:
        print("Duplicate value not inserted.")

    return root


# Create Binary Search Tree
def create_BST():

    root = None

    # Read number of nodes
    n = int(input("Enter number of nodes: "))

    # Insert all values
    i = 0
    while i < n:
        value = int(input("Enter value: "))
        root = insert(root, value)
        i = i + 1

    return root


# Non-Recursive Inorder Traversal
# Left -> Root -> Right
def inorder_non_recursive(root):

    if root is None:
        return

    stack = Stack()
    current = root

    while current is not None or not stack.is_empty():

        # Move towards leftmost node
        while current is not None:
            stack.push(current)
            current = current.left

        # Visit node at top of stack
        current = stack.pop()
        print(current.data, end=" ")

        # Move to right subtree
        current = current.right

    print()


# Non-Recursive Preorder Traversal
# Root -> Left -> Right
def preorder_non_recursive(root):

    if root is None:
        return

    stack = Stack()

    # Push root node
    stack.push(root)

    # Continue until stack becomes empty
    while not stack.is_empty():

        # Pop top node
        current = stack.pop()

        # Visit node
        print(current.data, end=" ")

        # Push right child FIRST
        if current.right is not None:
            stack.push(current.right)

        # Push left child
        if current.left is not None:
            stack.push(current.left)

    print()


# Main Algorithm
def main():

    # Create Binary Search Tree
    root = create_BST()

    print("Non-Recursive Inorder Traversal:")
    inorder_non_recursive(root)

    print("Non-Recursive Preorder Traversal:")
    preorder_non_recursive(root)


# Start program
main()
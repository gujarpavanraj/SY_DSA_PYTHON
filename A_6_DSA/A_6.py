
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def InsertNode(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = InsertNode(root.left, value)
    elif value > root.data:
        root.right = InsertNode(root.right, value)
    else:
        print("Duplicate Value")

    return root


def CopyTree(root):
    if root is None:
        return None

    newNode = Node(root.data)
    newNode.left = CopyTree(root.left)
    newNode.right = CopyTree(root.right)

    return newNode


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def Enqueue(self, data):
        newNode = QueueNode(data)

        if self.rear is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def Dequeue(self):
        if self.front is None:
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data

    def isEmpty(self):
        return self.front is None


def LevelOrder(root):
    if root is None:
        print("Tree is Empty")
        return

    Q = Queue()
    Q.Enqueue(root)

    while not Q.isEmpty():
        current = Q.Dequeue()
        print(current.data, end=" ")

        if current.left is not None:
            Q.Enqueue(current.left)

        if current.right is not None:
            Q.Enqueue(current.right)

    print()


def Height(root):
    if root is None:
        return -1

    leftHeight = Height(root.left)
    rightHeight = Height(root.right)

    if leftHeight > rightHeight:
        return leftHeight + 1
    else:
        return rightHeight + 1


def PrintLeafNodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return

    PrintLeafNodes(root.left)
    PrintLeafNodes(root.right)


def Main():
    root = None
    copyRoot = None
    choice = 0

    while choice != 7:
        print("\n===== Binary Search Tree Menu =====")
        print("1. Insert Node")
        print("2. Display Original BST (Level Order)")
        print("3. Copy BST")
        print("4. Display Copied BST (Level Order)")
        print("5. Find Height of BST")
        print("6. Print Leaf Nodes")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value: "))
            root = InsertNode(root, value)

        elif choice == 2:
            print("Original BST:")
            LevelOrder(root)

        elif choice == 3:
            copyRoot = CopyTree(root)
            print("BST Copied Successfully")

        elif choice == 4:
            print("Copied BST:")
            LevelOrder(copyRoot)

        elif choice == 5:
            print("Height of BST =", Height(root))

        elif choice == 6:
            print("Leaf Nodes:")
            PrintLeafNodes(root)
            print()

        elif choice == 7:
            print("Program Terminated")

        else:
            print("Invalid Choice")


Main()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                return  # duplicate value ignored

    def printTree(self):
        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            print(node.data, end=" ")
            inorder(node.right)

        inorder(self.root)
        print()


# Start the program
tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)

tree.printTree()

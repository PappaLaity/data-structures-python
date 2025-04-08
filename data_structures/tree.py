from data_structures.stack import Stack


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.__node = None

    def head(self):
        return self.__node

    def insert(self, item):
        temp = self.__node
        node = Node(item)
        if self.__node == None:
            self.__node = node
            head = self.__node
        else:
            head = self.__node
            if temp.data > item:
                # the value is smallest than the root and the left side is none
                if temp.left == None:
                    # Case of leaf node
                    print(f"Insert to left of node {temp.data}")
                    temp.left = node
                else:
                    # Case of parent node
                    print(f"Insert to left of root {temp.data}")
                    self.__node = temp.left
                    self.insert(item)
            if temp.data < item:
                # the value is greater than the root and the right side is none
                if temp.right == None:
                    # Case of leaf node
                    print(f"Insert to right of node {temp.data}")
                    temp.right = node
                else:
                    # Case of Parent node
                    print(f"Insert to rigth of root {temp.data}")
                    self.__node = temp.right
                    self.insert(item)
        self.__node = head

        # Check the value of head comparing to the node

    def search():
        pass

    def deleteNode(self, data):
        pass


def printInorder(b_tree) -> None:
    # left - root - right
    if b_tree:
        printInorder(b_tree.left)  # Traverse left subtree
        print(b_tree.data, end=" ")  # Visit node
        printInorder(b_tree.right)  # Traverse right subtree


def printPreOrder(b_tree):
    # root - left - right
    if b_tree:
        print(b_tree.data, end=" ")  # Visit node
        printInorder(b_tree.left)  # Traverse left subtree
        printInorder(b_tree.right)  # Traverse right subtree



def printPostOrder(b_tree):
    # left - right -root
    if b_tree:
        printInorder(b_tree.left)  # Traverse left subtree
        printInorder(b_tree.right)  #
        print(b_tree.data, end=" ")  # Visit node

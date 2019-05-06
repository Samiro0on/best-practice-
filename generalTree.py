


class BSTree:

    def __init__(self, nodeName, value):
        self.left = None
        self.right = None
        self.nodeName = nodeName
        self.value = value

    def get_left_child(self):
        return self.left


    def get_right_child(self):
        return self.right


    def set_node_value(self, val):
        self.value = val

    def get_node_value(self):
        return self.value

    def set_node_name(self, name):
        self.nodeName = name

    def get_node_name(self):
        return self.nodeName

    def set_left_child(self, leftName, val):
        if self.left == None:
            self.left = BSTree(leftName, val)
        else:
            newTree = BSTree(leftName, val)
            newTree.left = self.left
            self.left = newTree


    def set_right_child(self, rightName, val):
        if self.right == None:
            self.right = BSTree(rightName, val)
        else:
            newTree = BSTree(rightName, val)
            newTree.right = self.right
            self.right = newTree


    def add_node(self, xName, val):
        if val < self.value:
            self.set_left_child(xName, val= val)
        else:
            self.set_right_child(xName, val= val)

    def display_BinaryTree(self):
        self.get_node_name()
        self.get_left_child()
        self.get_right_child()
        self.get_node_value()

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if (node == None):
            self.root = Node(value)
        else:
            if (value < node.data):
                if (node.left == None):
                    node.left = Node(value)
                else:
                    self.addNode(node.left, value)
            else:
                if (node.right == None):
                    node.right = Node(value)
                else:
                    self.addNode(node.right, value)

    def display(self, node):
        if (node != None):
            self.display(node.left)
            print(node.data)
            self.display(node.right)

class Node:
    """ class to create a nodes for the tree"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class Queue:
    """class Queue which implements Queue data structure with its common methods"""

    def __init__(self):
        """Initiate class"""

        self.front = None
        self.rear = None

    def is_empty(self):
        """method to check if Queue is empty"""

        if self.front == None:
            return True
        return False

    def enqueue(self, node):
        """Method that takes any value as an argument and adds a new node with that value to the back of the queue """

        new_node = node

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns the node’s value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        """Method that returns the value of the node located in the front of the queue, 
        without removing it from the queue."""

        if not self.is_empty():
            return self.front.value
        return None


class BinaryTree:
    """Class to create a binary tree"""

    def __init__(self):
        self.root = None

    def pre_order(self, node=None, array_tree=None):
        """Recursive function to perform preorder traversal on the tree
           root >> left >> right
        """

        if array_tree is None:
            array_tree = []

        node = node or self.root

        # Display the data part of the root node
        array_tree.append(node.value)

        # Traverse the left subtree
        if node.left:
            self.pre_order(node.left, array_tree)

        # Traverse the right subtree
        if node.right:
            self.pre_order(node.right, array_tree)

        return array_tree

    def in_order(self, node=None, array_tree=None):
        """Recursive function to perform inorder traversal on the tree
           left >> root >> right
        """
        if array_tree is None:
            array_tree = []

        node = node or self.root

        if node.left:
            self.in_order(node.left, array_tree)

        array_tree.append(node.value)

        if node.right:
            self.in_order(node.right, array_tree)

        return array_tree

    def post_order(self, node=None, array_tree=[]):
        """Recursive function to perform postorder traversal on the tree
              left >> right >> root
        """

        node = node or self.root

        if node.left:
            self.post_order(node.left, array_tree)

        if node.right:
            self.post_order(node.right, array_tree)

        array_tree.append(node.value)

        return array_tree


class BinarySearchTree(BinaryTree):
    """Class to create a Binary Search Tree """

    def add(self, value):
        """Method that accepts a value, and adds a new node with that value in the correct location 
        in the binary search tree"""

        node = Node(value)
        if self.root == None:
            self.root = node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    break
            else:  # value >= current.value
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    break

    def contains(self, value):
        """Method that accepts a value, and returns a boolean indicating whether or not the value is 
        in the tree at least once."""

        if self.root == None:
            raise myException("Tree is empty")

        current = self.root

        while current:

            if current.value == value:
                return True

            if current.value > value:
                current = current.left

            else:
                current = current.right
        return False


class myException(Exception):
    """Exception class to handle empty tree"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

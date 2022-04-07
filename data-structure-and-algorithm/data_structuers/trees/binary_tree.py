class _Node:
    """Private class to create a nodes for the tree"""

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
        """Method that returns the value of the node located in the front of the queue, without removing it from the queue."""

        if not self.is_empty():
            return self.front.value
        return None


class BinaryTree:
    """Class to create a binary tree"""

    def __init__(self):
        self._root = None

    def pre_order(self, node=None, arr=None):
        """Method to return an array of tree values in "pre-order" order"""
        pass

    def in_order(self, node=None, arr=None):
        """Method to return an array of tree values "in-order" """
        pass

    def post_order(self, node=None, arr=[]):
        """Method to return an array of tree values "post-order" """
        pass


class BinarySearchTree(BinaryTree):
    """Class to create a Binary Search Tree """

    def add(self, value):
        """Method that accepts a value, and adds a new node with that value in the correct location in the binary search tree"""
        pass

    def contains(self, value):
        """Method that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once."""
        pass


class myException(Exception):
    pass

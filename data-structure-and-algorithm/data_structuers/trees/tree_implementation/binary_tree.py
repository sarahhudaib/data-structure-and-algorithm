class Node:
    """ class to create a nodes for the tree"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class BinaryTree:
    """Class to create a binary tree"""

    def __init__(self, value=None):
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

    def findMax(self):
        """ Finds the maximum value in a binary tree """
        return self.pre_order(self.root)[-1]  # will return the last element in the list of pre_order


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


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(88)
    tree.add(11)
    tree.add(13)
    tree.add(99)
    tree.add(-25)
    tree.add(102)
    tree.add(19)
    tree.add(17)
    tree.add(23)
    tree.add(55)
    tree.add(77)
    tree.add(2)
    print(tree.findMax())
    # [88, 11, 13, -25, 2, 17, 19, 23, 55, 77, 99, 102]
    print(tree.pre_order())

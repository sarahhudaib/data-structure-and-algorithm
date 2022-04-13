class Node:
    """ class to create a nodes for the tree"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Class to create a binary tree"""
    def __init__(self, value=None):
        self.root = None
    
    def findMax(self,root):
        """Find the max value in the tree"""
        if (root == None):
            return float('-inf')

        res = root.value
        lres = self.findMax(root.left)
        rres = self.findMax(root.right)
        if (lres > res):
            res = lres
        if (rres > res):
            res = rres
        return res


if __name__ == '__main__':
    BT= BinaryTree()
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)
    
    print("Maximum element is",BT.findMax(root))

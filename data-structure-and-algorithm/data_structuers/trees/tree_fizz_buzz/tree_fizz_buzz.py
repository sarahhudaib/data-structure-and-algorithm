class Node:
    """ This class is used to create a node in the tree """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """ This class is used to create a binary tree """

    def __init__(self):
        self.root = None


def fizz_buzz(k):
    """This function is used to change the k according to fizz_buzz

        input: k    
        output: k according to fizz_buzz
    """
    if (k % 5 == 0) and (k % 3 == 0):
        return "FizzBuzz"
    if k % 5 == 0:
        return "Buzz"
    if k % 3 == 0:
        return "Fizz"
    return str(k)


def tree_fizz_buzz(default_tree):
    """This function is used to change the value according to fizz_buzz to handle the edge case of the tree

        input: default_tree
        output: default_tree with the value according to fizz_buzz
    """
    updated_tree = BinaryTree()

    if not default_tree.root:
        return updated_tree  # if the tree is empty

    def walk(current):
        """This function used to add new nodes to the tree according to fizz_buzz and the value of the node

            input: current
            output: current with the value according to fizz_buzz
        """
        node = Node(fizz_buzz(current.value))

        if current.left:
            node.left = walk(current.left)
        if current.right:
            node.right = walk(current.right)
        return node

    updated_tree.root = walk(default_tree.root)
    return updated_tree

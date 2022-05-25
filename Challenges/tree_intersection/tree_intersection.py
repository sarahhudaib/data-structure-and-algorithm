class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.ans = []

    def pre_order(self):
        node = self.root

        def walk(node):
            self.ans.append(node.value)
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)

        walk(node)
        return self.ans


"""
check if both trees have a root node
convert  tree1 to a set
convert  tree2 to a set
create an empty list to store the intersection
iterate through the list
check if the element is in the set
if it is, add it to the list
convert the list to a set and return it
if either tree doesn't have a root node return a message
"""


def tree_intersection(tree1, tree2):
    """Function to find the intersection of two trees
       Input: tree1 and tree2
       Output: list of values that are in both trees
    """
    if tree1.root and tree2.root:
        set1 = set(tree1.pre_order())
        set2 = tree2.pre_order()
        ans = []
        for i in set2:
            if i in set1:  # if i is in set1, add it to the list
                ans.append(i)
        return set(ans)
    else:
        return ('This tree is empty')


if __name__ == '__main__':
    binary_tree = BinaryTree()
    binary_tree.root = Node(10)
    binary_tree.root.right = Node(20)
    binary_tree.root.left = Node(30)
    binary_tree.root.left.left = Node(40)
    binary_tree.root.left.right = Node(50)
    binary_tree.root.left.right.left = Node(60)
    binary_tree.root.left.right.right = Node(70)
    binary_tree.root.right.left = Node(80)
    binary_tree.root.right.right = Node(90)
    binary_tree.root.right.right.left = Node(100)

    binary_tree1 = BinaryTree()
    binary_tree1.root = Node(101)
    binary_tree1.root.right = Node(20)
    binary_tree1.root.left = Node(301)
    binary_tree1.root.left.left = Node(40)
    binary_tree1.root.left.right = Node(501)
    binary_tree1.root.left.right.left = Node(60)
    binary_tree1.root.left.right.right = Node(701)
    binary_tree1.root.right.left = Node(80)
    binary_tree1.root.right.right = Node(901)
    binary_tree1.root.right.right.left = Node(100)

    print(tree_intersection(binary_tree, binary_tree1))

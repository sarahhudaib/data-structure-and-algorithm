from tree_max import BinaryTree, Node

def test_find_max_tree():
    BT= BinaryTree()
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)
    expected = BT.findMax(root)
    actual = 11
    assert actual == expected
    
    
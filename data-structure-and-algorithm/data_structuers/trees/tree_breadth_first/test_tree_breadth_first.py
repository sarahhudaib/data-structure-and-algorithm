from tree_breadth_first import BinaryTree, breadth_first


def test_breadth_first():
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)

    assert breadth_first(tree._root) == [[1], [2, 3], [4, 5]]


def test_add_four_nodes():
    tree = BinaryTree()
    tree.add('apples')
    tree.add('bananas')
    tree.add('cucumbers')
    tree.add('dates')
    assert tree._root.value == 'apples'
    assert tree._root.left.value == 'bananas'
    assert tree._root.right.value == 'cucumbers'
    assert tree._root.left.left.value == 'dates'
    assert tree._root.left.right == None

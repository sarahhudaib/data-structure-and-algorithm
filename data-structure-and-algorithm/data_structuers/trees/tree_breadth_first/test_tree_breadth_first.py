from tree_breadth_first import BinaryTree, Node , BinarySearchTree
import pytest

def test_breadth_first_binarytree_with_letters():
    tree = BinaryTree()
    tree._root = Node(2)
    tree._root.left = Node(7)
    tree._root.right = Node(5)
    tree._root.left.left = Node(2)
    tree._root.left.right = Node(6)
    tree._root.right.right = Node(9)
    tree._root.left.left.left = Node(5)
    tree._root.left.left.right = Node(11)
    tree._root.right.right.right = Node(4)
    assert BinaryTree.breadth_first(tree) == [2, 7, 5, 2, 6, 9, 5, 11, 4]

def test_breadth_first_binarysearch(my_bst):
   assert BinaryTree.breadth_first(my_bst) == [15, 11, 19, 7, 13, 17, 23, 5, 8]
   
   
@pytest.fixture
def my_bst():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(11)
    tree.add(13)
    tree.add(7)
    tree.add(8)
    tree.add(5)
    tree.add(19)
    tree.add(17)
    tree.add(23)


    return tree
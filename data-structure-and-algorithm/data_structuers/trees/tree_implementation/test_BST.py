from binary_tree import BinaryTree, BinarySearchTree
import pytest


def test_tree_instance():
    """Can successfully instantiate an empty tree"""
    tree = BinaryTree()
    assert tree.root is None


def test_tree_single_nodes():
    """Can successfully instantiate a tree with a single root node"""
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree.root.value == 'apples'


def test_add_left_right_nodes():
    """can successfully add a left child and right child properly to a node"""
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15


def test_pre_order(test_BST):
    """Can successfully return a collection from a preorder traversal"""
    assert test_BST.pre_order() == [15, 11, 7, 5, 8, 13, 19, 17, 23]


def test_in_order(test_BST):
    """Can successfully return a collection from an inorder traversal"""
    assert test_BST.in_order() == [5, 7, 8, 11, 13, 15, 17, 19, 23]


def test_post_order(test_BST):
    """Can successfully return a collection from a postorder traversal"""
    assert test_BST.post_order() == [5, 8, 7, 13, 11, 17, 23, 19, 15]


def test_add_one_node():
    """Can successfully add a single node to a tree"""
    tree = BinarySearchTree()
    tree.add(20)
    assert tree.root.value == 20
    assert tree.root.left == None
    assert tree.root.right == None


def test_contains_true(test_BST):
    """Can successfully return true for a value in the tree"""
    assert test_BST.contains(7) == True


def test_contains_false(test_BST):
    """Can successfully return false for a value in the tree"""
    assert test_BST.contains(9) == False

# ------------------------------------------------


def test_find_max():
    """Can successfully return the maximum value in the tree"""
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

    actual = tree.findMax()
    Expected = 102
    assert actual == Expected


@pytest.fixture
def test_BST():
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
